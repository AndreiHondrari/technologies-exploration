# Polling with zero delay

## Constituents

- a sender that sends messages at regular interval
- a receiver that polls without any delay

## How to test

- start the receiver
- start the sender for a few seconds and then stop
- repeat last step as many times as you like

## Observations

- the poll with zero delay simply checks if there is anything and then continues
- good for infinite loops
