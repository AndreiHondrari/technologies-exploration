# Requesters to router

## Overview

A bunch of requesters send requests to a router. The router unpacks the messages
and then replies to each of the requesters.

The requester runs once. The repliers run in a loop.

## How to test

- start several requesters
- start the router

## Observations

- you have to keep in mind the address of the requester that you got the message
  from via the router, so you know to whom to reply
