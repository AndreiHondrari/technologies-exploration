# Simple heartbeat

## Overview

The server registers nodes as they connect and send a greeting, and sends
messages to them.

If a node disconnects the server notices that the heartbeat does not get a
response, so fails the node from its presence.
