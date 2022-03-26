# 1 publisher and two filtered subscriber clients

## Overview

The server/publisher, binds and sends events.

The clients connect/subscribe to the server and configure a filter.

## How to test

- spawn client_a
- spawn client_b
- spawn publisher

Notice that the two clients receive different messages. The messages that they
receive are according to the setsockopt(ZMQ_SUBSCRIBE, "...category...") that
they've specified

## When to use this

When you want different nodes to receive specific messages.

## Some examples

- logger that considers only critical errors for monitoring
- news client that wants articles only from specific vendors
