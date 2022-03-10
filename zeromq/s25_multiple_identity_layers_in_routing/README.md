# Multiple identity layers due to multiple routers

## Overview

### Constituents:

- three brokers (A, B and C)
- a requester
- a replier

### Flow of requests and replies

```mermaid
flowchart LR
  X[Requester]
  Y[Replier]

  A[Broker 1]
  B[Broker 2]
  C[Broker 3]

  X -- req --> A
  A -- rep --> X
  A -- req --> B
  B -- rep --> A
  B -- req --> C
  C -- rep --> B
  C -- req --> Y
  Y -- rep --> C
```

## Test sequence diagram

```mermaid
sequenceDiagram

  actor T as Tester

  participant X as Requester

  participant A as Broker 1
  participant B as Broker 2
  participant C as Broker 3

  participant Y as Replier

  %% brokers initialization
  T ->>+ A: start
  T ->>+ B: start
  T ->>+ C: start

  %% replier initiatialization
  T ->>+ Y: start

  %% test sequence 1

  T ->>+ X: start
  X ->>+ A: request 1
  A ->>+ B: request 1
  B ->>+ C: request 1
  C ->>+ Y: request 1
  Y -->- C: reply to 1
  C -->- B: reply to 1
  B -->- A: reply to 1
  A -->- X: reply to 1
  X ->>- X: stop

  T ->>+ X: start
  X ->>+ A: request 2
  A ->>+ B: request 2
  B ->>+ C: request 2
  C ->>+ Y: request 2
  Y -->- C: reply to 2
  C -->- B: reply to 2
  B -->- A: reply to 2
  A -->- X: reply to 2
  X ->>- X: stop

  % restart broker 2
  T ->> B: Ctrl + C
  B ->>- B: stop

  T ->>+ B: start

  % test sequence 2

  T ->>+ X: start
  X ->>+ A: request 3
  A ->>+ B: request 3
  B ->>+ C: request 3
  C ->>+ Y: request 3
  Y -->- C: reply to 3
  C -->- B: reply to 3
  B -->- A: reply to 3
  A -->- X: reply to 3
  X ->>- X: stop

  T ->>+ X: start
  X ->>+ A: request 4
  A ->>+ B: request 4
  B ->>+ C: request 4
  C ->>+ Y: request 4
  Y -->- C: reply to 4
  C -->- B: reply to 4
  B -->- A: reply to 4
  A -->- X: reply to 4
  X ->>- X: stop

  %% final close  
  T ->> Y: Ctrl+C
  Y ->>- Y: stop

  T ->> C: Ctrl+C
  C ->>- C: stop

  T ->> B: Ctrl+C
  B ->>- B: stop

  T ->> A: Ctrl+C
  A ->>- A: stop
```

## How to test

- start all the brokers
- start the replier
- run the requester two times
- restart broker 2
- run the requester two times

## Observations

- broker 1 receives from the router socket a multipart in the following format
  `[requester_address, b'', msg]`
- broker 2 receives from the router socket a multipart in the following format
  `[broker_1_address, requester_address, b'', msg]`
- broker 3 receives from the router socket a multipart in the following format
  `[broker_2_address, broker_1_address, requester_address, b'', msg]`
- essentially, the more brokers we have, the more addresses are prefixed to each
  of the messages
- the router strips each address layer when returning back to the originating
  dealer or the actual requester
- each new instance of the requester generates a new address:
  - `b'\x00\x80\x00A\xa7'`
  - `b'\x00\x80\x00A\xa8'`
  - `b'\x00\x80\x00A\xa9'`
  - `b'\x00\x80\x00A\xaa'`
- the same kind of address increment happens to the brokers. See how broker 3
  sees broker 2 before and after restart:
  - before: `b'\x00\x80\x00A\xa7'`
  - after: `b'\x00\x80\x00A\xa8'`
