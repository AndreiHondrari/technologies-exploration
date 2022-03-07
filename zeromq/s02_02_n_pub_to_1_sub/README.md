# N publishers to 1 subscriber

## Overview

The subscriber binds and receives.

The publishers connect to the subscriber and send.

## How to test

- spawn 1 subscriber
- spawn multiple publishers

Observe that the subscriber is ingesting all the messages coming from the
publishers.

## When to use this

When you want to gather events from multiple publishers.

## Some examples

- centralized logging
- centralized monitoring
