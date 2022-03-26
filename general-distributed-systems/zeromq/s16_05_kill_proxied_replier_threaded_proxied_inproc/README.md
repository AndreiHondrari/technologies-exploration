# Kill threaded replier (with embedded proxy)

## Overview

Consists of:

- a normal requester
- a replier service that runs a proxy in the main thread and a replier socket in
  a slave thread

## How to test

- start the replier service and the requester
- kill the replier service
- restart the replier service

## Observations

- when the replier and the proxy are closed, the requester waits patiently until
  the service is restarted
