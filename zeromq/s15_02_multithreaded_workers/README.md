# Multithreaded REQ/REP dynamic worker repliers

## Overview

- A service that waits for connections and messages from multiple requesters and
  passes them via a ROUTER/DEALER broker to multiple threads that act as
  repliers

- requesters that connect to the service and make requests and wait for replies

## How to test

- start the service
- start multiple requesters

## When to use this

When you want to start a service faster by running only one program, instead of
multiple programs, and when you want to vary the number of workers by varying
the number of threads.

## Some examples

- a clearly defined service to provide answers for multiple requesters
