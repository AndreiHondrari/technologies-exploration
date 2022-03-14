# REQ as receiver with ROUTER as sender

## Overview

First example on dynamic address discovery for the router. The address is
discovered right after the requester connects to the router (binder), and sends
a first greeting message. The ROUTER picks up this first message and captures
the address of the sender.

The ROUTER can now proceed to send something of value to the receiver (REQ
node).

In this scheme, the REQ node can use the recv as a means of input for doing
stuff, and send as a means of replying back to the dispatcher (ROUTER node).

## How to test

- start the router
- start the requester several times (you can use a single terminal because it
  ends fast)

## Observations

- the ROUTER can keep track of how many peers connected to it and make decisions
  on what to send to whom
