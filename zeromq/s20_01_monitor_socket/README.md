# Socket monitor

## Overview

- a replier with an attached monitor
- a requester with an attached monitor

## How to test

- run the replier
- run the requester
- stop the requester
- restart the requester
- stop the replier

## Observations

Both the requester and the replier display a series of events like:

- EVENT_CONNECT_RETRIED
- EVENT_CLOSED
- EVENT_CONNECTED
- EVENT_HANDSHAKE_SUCCEDED
- EVENT_DISCONNECTED

## When to use this

When we want to perform certain actions on connection/disconnection of nodes.

## Some examples

- all subscribers disconnected so there is no need to issue events anymore
- sink disconnected so workers should halt processing for the moment, until the
  sink reconnects again
