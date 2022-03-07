# Non-polling multi socket read

## Overview

There are two senders that bind as PUSH and send delayed messages (in blocking
mode).

There is one reader that connects to both senders and reads continuously (in an
event loop) from both sockets (in non-blocking mode).

## How to test

- Start the reader
- Start both senders

Notice that the reader processes the message from any of the senders as soon as
it gets it. This is similar to N Requesters to 1 replier, but the difference is
that the reader does not wait in this case, and will happily process from any of
the senders, in any order. The REQ/REP also does this, but in this case you have
explicit sockets to specific nodes, hence you have a "hardwired" connection.

## When to use this

When you know exactly what nodes you will connect to and they have a very
specific purpose, and you want to handle messages from them in specific ways, no
matter in what order these messages come from these explicit senders.

## Some examples

- funnel messages coming from distinct nodes and focus them as one stream
- notify classes of subscribers that are interested in specific events from
  specific senders (perhaps even subscribing/unsubscribing dynamically)
- in a smart house, send messages to a specific set of lamps when the sensor in
  a room detects the presence of a person and notifies that event. Each room
  will have a sensor and each sensor has a specific socket in our script. Since
  multiple people can be in different rooms at the same time, the asynchronous
  receipt of the presence events and asynchronous issuing of the commands is
  therefore desirable
