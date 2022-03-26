# 1 Requester to N repliers

## Overview

One requester sends requests to multiple repliers in a round-robin fashion.

The requester binds for listen.

The repliers connect to the requester.

## How to test

- spawn a requester
- spawn multiple repliers

## When to use this

When you want to distribute some tasks evenly between multiple workers.

## Some example use cases

- update clones with the same new information
- ask multiple nodes of their situation to assess and reach a conclusion
