# 1 Publisher to N subscribers

## Overview

Publisher binds and sends.

Subscribers connect to the publisher and receive.

## How to test

- spawn the publisher
- spawn multiple subscribers

You will observe that all the subscribers receive the same message when
published by the publisher.

IMPORTANT: Notice that the first message is not received by the subscribers, due
to the fact that it takes time for the handshake to happen.

## When to use this

- Intended for one way communication (as opposed to REQ/REP pattern).

- When you want multiple receivers to get the same information at the same time.

## Some examples

- sending a search query to search nodes that have different shards of
  information
- notifying clients of an update
- broadcast command (turn all lights off)
