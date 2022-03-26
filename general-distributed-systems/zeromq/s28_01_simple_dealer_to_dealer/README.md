# Dealer to dealer - simple

## Overview

A bunch of dealers communicate with a central dealer.

## Flowchart

```mermaid
flowchart
  X[Central dealer]

  A[Node dealer 1]
  B[Node dealer 2]
  N[Node dealer n]

  X <--> A
  X <--> B
  X <--> N
```

## How to test

- start the server
- start a node
- stop the node
- start another node
- stop the server

## Observations

- client-type of dealers will keep sending (until the HWM is hit), without the
  server up and running
