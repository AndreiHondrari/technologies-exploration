# Polling multi socket reader

## Overview

There are two senders that bind as PUSH and send delayed messages (in blocking
mode).

There is one reader that connects to both senders (in PULL mode) and reads
continuously (in an event loop) from both sockets (also in blocking mode). The
reader makes use of a poller to determine if there are any new messages on the
pipe, from any of the registered senders.

## How to test

- start the reader
- start the two senders

## Observation

Notice that the reader receives messages from both senders in any order.

In this case however, there is no infinite loop that will constantly try to recv
from both sockets in non-blocking mode, passing when EAGAIN is triggered, but
rather uses an internal infinite loop, via a poller utility that will constantly
check if there are messages on the buffers of any of the sockets.

## When to use this

Same like non polling multi socket reader
