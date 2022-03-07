# Delayed receiver start-up

## Overview

The receiver binds as PULL and polls for new messages. As soon as a message is
seen on the buffer, it tries to empty it.

The sender keeps sending multipart messages consisting of 3 parts (connected to
the receiver in PUSH mode).

## How to test

- start the sender and wait for it to send several multipart messages.
- start the receiver

## Observation

The receiver just ingests all the parts that the sender sent, without regard of
delimitation of these multipart messages.

# Warning

This can be a problem if you want to have these messages treated as separate
entities

## When to use this
