# PAIR sockets for unrestricted/unordered bidirectional communication

## Overview

Two threads, programs, nodes that communicate over a PAIR type of sockets.

## How to test

- run the main

## Observations

- PAIR sockets send and receive between threads
- PAIR sockets can send and receive in both directions in any order, not being
  constrained like REQ/REP to first request/receive or receive/reply.

## When to use this

When you want to define your own bidirectional sequence of sends and receives
between two nodes.
