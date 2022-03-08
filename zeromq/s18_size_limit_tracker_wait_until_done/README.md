# Track send

## Overview

Our constituents:

- a sender that sends a large chunk of data while tracking
- a receiver that waits for a message and then copies an incoming message from
  the buffer

## How to test

- start the receiver
- start the sender several times subsequently (it runs one time - no loop)

## Observations

As soon as the message is passed from the sender to the receiver we obtain the
following effects:

- in the receiver: the tracker wait call releases
- in the sender: the poll releases
- both of them release at the same time

## When to use this

When we want to synchronise based on the send process.

## Some examples

- a transaction in the database that a specific chunk of data was sent and
  perhaps allowing us to rollback in case of failure
