# Envelope in pub/sub

## Overview

Our constituents:

- a publisher that sends a message and the prefix as multipart
- a subscriber that subscribes to a specific topic and receives multipart

## How to test

- start a subscriber
- start a publisher

## Observations

Our message is clearly isolated from the filtering key.

## When to use this

When we want to have a clear separation of data.
