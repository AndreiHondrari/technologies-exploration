# Multipart auto

## Overview

Receiver binds as PULL and starts receiving multipart messages (as bytes).

Sender connects to receiver in PUSH mode and starts sending multipart messages.

## How to test

- start a receiver
- start sender(s)

## Observation

Sender sends whole, clearly delimited multipart messages. Receiver gets whole,
clearly delimited multipart messages.

## When to use this

When you want to send messages that have envelopes, necessary for routing for
example.
