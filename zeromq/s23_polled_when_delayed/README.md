# Polling with delay in process

## Constituents

- a sender that sends messages at regular interval
- a receiver that polls for new messages and then processes with a time delay.
  The receive part does not occur in a loop after polling, but only a single
  time.

The sender sends more frequent than the receiver is able to process.

## How to test

- start the receiver
- start the sender for a few seconds and then stop
- wait until the receiver seems to have finished the messages processing
- repeat last two steps as many times as you like

## Observations

- the receival of a message does not invalidate the polling itself, but rather
  informs us that there are still messages in the buffer
