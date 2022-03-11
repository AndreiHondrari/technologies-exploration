# Dealer to dealer

## Overview

Asynchronous send and receive between a central dealer and distributed dealers.

One can send as many times from the dealer and then receive many times from the
distributed dealer nodes.

## Diagram

```mermaid
flowchart
  X[Central dealer]

  A[Worker dealer 1]
  B[Worker dealer 2]

  X -- send --> A
  X -- send --> B

  A -- reply 1 --> X
  A -- reply 2 --> X
  A -- reply n --> X

  B -- reply 1 --> X
  B -- reply 2 --> X
  B -- reply n --> X
```

## Test sequence diagram

```mermaid
sequenceDiagram
  actor T as Tester

  participant X as Central Dealer
  participant A as Worker Dealer 1
  participant B as Worker Dealer 2

  %% initialization
  T ->>+ A : start
  T ->>+ B : start
  T ->>+ X : start

  %% tasks
  X ->>+ A : send
  X ->>+ B : send

  par
    loop Worker 1 sends 9 values
      A -->> X : send a value
      X ->> X : display value
    end
  and
    loop Worker 2 sends 9 values
      B -->> X : send a value
      X ->> X : display value
    end
  end

  X ->>- X : stop

  %% cleanup
  T ->> A : Ctrl+C
  A ->>- A : stop
  T ->> B : Ctrl+C
  B ->>- B : stop
```

## How to test

- open two worker dealers
- open the central dealer

## Observations

- the central dealer and the worker dealer can send and receive any number of
  times (of course within the limit of the buffer), and in any order as desired
- create an asynchronous way of dealing with sends and receives (compared to
  REQ/REP where you either mandatory have to send after a receive or receive
  after a send)
- you must keep in mind yourself for what is the reply destined, hence you need
  to use some sort of tracking ID
