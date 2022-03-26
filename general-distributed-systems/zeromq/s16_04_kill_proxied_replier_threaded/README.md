# Kill threaded replier

## Overview

Consists of:

- a normal requester and proxy.
- a replier that lives inside a thread.

## How to test

- start proxy, replier and requester
- kill the replier
- restart the replier

## Observations

- when the threaded replier dies, the communication pauses
- when the threaded replier restarts, the communication also resumes
