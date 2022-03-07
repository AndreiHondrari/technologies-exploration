# N requesters to 1 replier

## Overview

The replier binds for listening.

The requesters connect to the replier and send requests.

The more requesters, the more they have to wait, because the replier has to
service more requests.

## How to test

- spawn 1 replier
- spawn multiple requesters

## When to use this setup

When 1 replier process is enough to serve multiple requesters, given that the
number of requesters does not result in an excessive amount of requests.

Usually a replier should be able to accept around 10000 requests per second.
Serving a request also depends on what actually happens in the request
processing part.
