# Ventilator

## Overview

A sink that binds and waits for messages from workers.

Several workers that connect to a ventilator and a sink, waiting for messages
for processing from the ventilator, and after processing sending the result to
the sink.

## How to test

- spawn a sink
- spawn several workers
- spawn the ventilator

The ventilator will spread several messages to all the workers, which will
receive the messages in a round-robin fashion, "process"

## When to use this

When you have a node that has a high volume of messages to be sent, and you need
a long time to process each message, hence you need to spawn multiple
processors/workers.

## Some example use cases

- sending different queries to database search nodes (that connect to the same
  database)
- splitting the processing of a heavy simulation between multiple computers
  (with GPU for e.g.)
