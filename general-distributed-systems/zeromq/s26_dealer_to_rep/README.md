# Dealer to REP

## Overview

A dealer distributes messages to several repliers. It sends as many as it wants
and it receives everything afterwards.

## Constituents

- a dealer that sends a given amount of iterations, and receives the same amount
  in a secondary sequence
- multiple repliers that get the messages from the dealer in a round-robin
  fashion

## Flow diagram

```mermaid
flowchart TB
  X[Dealer]

  A[Replier 1]
  B[Replier 2]
  C[Replier 3]

  X -- req --> A
  X -- req --> B
  X -- req --> C

  A -- rep --> X
  B -- rep --> X
  C -- rep --> X
```

## Test sequence diagram

```mermaid
sequenceDiagram
  actor T as Tester

  participant X as Dealer
  participant A as Replier 1
  participant B as Replier 2
  participant C as Replier 3

  %% init
  T ->>+ X : start
  T ->>+ A : start
  T ->>+ B : start
  T ->>+ C : start

  %% startup
  X ->>+ X : wait
  A ->> X : connect
  B ->> X : connect
  C ->> X : connect
  X ->>- X : wait_done

  %% nodes communication
  par Dealer and Repliers
    X ->> X : enqueue 1
    X ->> X : enqueue 2
    X ->> X : enqueue 3
    X ->> X : enqueue 4
    X ->> X : enqueue 5
  and
    X ->> A : send 1
    X ->> B : send 2
    X ->> C : send 3
    X ->> A : send 4
    X ->> B : send 5
  and
    A -->> X : reply 1
    B -->> X : reply 2
    C -->> X : reply 3
    A -->> X : reply 4
    B -->> X : reply 5
  end

  %% recv sequence
  X ->> X : dequeue 1
  X ->> X : dequeue 2
  X ->> X : dequeue 3
  X ->> X : dequeue 4
  X ->> X : dequeue 5

  %% cleanup
  T ->> X : Ctrl+C
  X ->>- X: stop

  T ->> A : Ctrl+C
  A ->>- A : stop

  T ->> B : Ctrl+C
  B ->>- B : stop

  T ->> C : Ctrl+C
  C ->>- C : stop
```

## How to test

- start the repliers
- start the dealer

## Observations

- the dealer will distribute the messages in the round robin fashion to all
  repliers
- we have to wait a bit at the start of the dealer, to allow all the repliers to
  connect with the dealer in the background
- we have to send an en empty frame at the beginning of the multipart sequence,
  to indicate that this is a "REQ" type of frame, otherwise our replier will
  discard it
