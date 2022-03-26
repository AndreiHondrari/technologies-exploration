# Dynamic pub-sub

## Overview

A proxy that binds on different addresses. One proxy socket in in XSUB mode and
one proxy socket is in XPUB mode. The two sockets are bound via the utility
function `zmq.proxy(s1, s2)`.

Subscribers that connect to the proxy (XPUB side) in SUB mode and that start
listening to events.

Publishers that connect to the proxy (XSUB side) in PUB mode and start sending
events.

## How to test

- start the proxy
- start several subscribers
- start several proxies

## Observation

Notice that you can add as many publishers and subscribers as you want.

The subscribers will happily ingest all the events that come from multiple
publishers.

The proxy does all the heavy lifting of gathering and dispersing events.

## When to use this

When you might have to add multiple nodes that emit events, yet you don't know
the exact number of nodes needed.

## Some examples

- multiple sensors in a smart house that are connected one by one at different
  times
- multiple workers of a webservice that want to log events happening on them,
  which are spawned/terminated dynamically by the cloud infrastructure
