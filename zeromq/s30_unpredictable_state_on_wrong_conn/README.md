# Unpredictable state on wrong connection pair

## Overview

When we try to connect two types of sockets that aren't meant to be together, we
end up in a state that is unpredictable.

Examples of socket pairs that don't match

- REP with ROUTER
- REQ with DEALER
- PULL/PUSH with ROUTER
- PUB with REQ

## Constituents

```mermaid
flowchart LR
  A[Connecter]
  B[Binder]

  A <--> B
```

## Test sequence diagram

### Positive flow

```mermaid
sequenceDiagram

  actor T as Tester

  participant C as Connecter
  participant B as Binder

  T ->> T : select a valid pair of socket types
  T ->>+ C : start

  loop For ever (until SIGINT/SIGKILL)
    loop Until Binder listens and connect happens
      C ->> C : try connect to binder
      C ->> C : EVENT_CONNECT_RETRIED
      C ->> C : EVENT_CONNECT_DELAYED
    end

    T ->>+ B : start

    B ->> B : listen
    B ->> B : EVENT_LISTENING

    C ->> B : connect
    B -->> C : accept
    B ->> B : EVENT_ACCEPTED
    C ->> C : EVENT_CONNECTED

    C --> B : handshake
    C ->> C : EVENT_HANDSHAKE_SUCCEEDED
    B ->> B : EVENT_HANDSHAKE_SUCCEEDED

    T ->> B : Ctrl+C
    B -->> C : disconnect
    B ->> B : EVENT_DISCONNECTED
    C ->> C : EVENT_DISCONNECTED

    B ->>- B : stop
  end

  T ->> C : Ctrl+C
  C ->>- C : stop
```

### Negative flow

```mermaid
sequenceDiagram

  actor T as Tester

  participant C as Connecter
  participant B as Binder

  T ->> T : select invalid pair of socket types
  T ->>+ C : start

  loop Until Binder listens and connect happens
    C ->> C : try connect to binder
    C ->> C : EVENT_CONNECT_RETRIED
    C ->> C : EVENT_CONNECT_DELAYED
  end

  T ->>+ B : start

  B ->> B : listen
  B ->> B : EVENT_LISTENING

  C ->> B : connect
  B -->> C : accept
  B ->> B : EVENT_ACCEPTED
  C ->> C : EVENT_CONNECTED

  C --> B : handshake
  Note over C,B : pipe brakes

  B --> C : disconnect

  C ->> C : EVENT_DISCONNECTED
  B ->> B : EVENT_HANDSHAKE_FAILED_NO_DETAIL
  B ->> B : EVENT_DISCONNECTED

  loop Indefinite
    Note over C : Invalid state
  end

  T ->> B : Ctrl+C
  B ->>- B : stop

  %% secondary attempt with the binder
  T ->>+ B : start
  B ->> B : listen
  B ->> B : EVENT_LISTENING
  loop Indefinite
    Note over B : Nothing happens
  end
  T ->> B : Ctrl+C
  B ->>- B : stop

  T ->> C : Ctrl+C
  C ->>- C : stop
```

## How to test the negative flow

- start the connecter
- start the binder and let it stabilise
- stop the binder
- start the binder and let it stabilise

## Observations

- after starting the connecter, it continuously tries to connect and emits
  **EVENT_CONNECT_RETRIED** and **EVENT_CONNECT_DELAYED** in a loop
- after starting the binder:
  - connecter emits:
    - **EVENT_CONNECTED**
    - **EVENT_DISCONNECTED**
  - binder emits:
    - **EVENT_ACCEPTED**
    - **EVENT_HANDSHAKE_FAILED_NO_DETAIL**
    - **EVENT_DISCONNECTED**
  - binder displays the reason for the error as: _**Broken pipe**_
