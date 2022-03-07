# Dynamic Request/Reply

## Overview

One broker sitting in the middle, binding on two different addresses, one socket
in ROUTER mode, and one socket in DEALER mode. The broker passes messages from
ROUTER to DEALER or from DEALER to ROUTER, depending on which side loads
messages into the buffer.

Several requesters that connect to the ROUTER socket of the broker and perform
request/receive in a loop.

Several repliers that connect to the DEALER socket of the broker and perform
receive/reply in a loop.

## How to test

- spawn the broker
- spawn several repliers
- spawn several requesters

## Observation

- The messages from the requesters are spread between the repliers.
- The repliers know exactly to what requesters to reply, due to the fact that
  the messages are wrapped in an envelope with extra "node address" information
  that the broker DEALER and ROUTER sockets know where to pass.
- The DEALER distributes messages in round-robin fashion amongst the repliers

## When to use this

When you want to dynamically alter the number of nodes on both the requesters
and repliers side.

## Some examples

- repliers server nodes get overloaded and you want to add more workers to
  facilitate the increasing number of requesters or requests coming from these
  requesters.
