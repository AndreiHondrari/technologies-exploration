# one dealer to many routers

## Overview

Send messages from one dealer (binder) to many routers (connecters)

## Diagram

```mermaid
flowchart
  D[Dealer]

  A[Router 1]
  B[Router 2]
  N[Router n]

  D --> A
  D --> B
  D --> N
```

## How to test

- start a couple of routers
- start a dealer

## Observations

- the dealer will send continuously until the HWM is hit
- the routers will receive the messages but only as multipart
