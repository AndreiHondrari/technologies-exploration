# Disconnecting mid-air

## Overview

The receiver tries to connect to a sender and waits for a message.

The sender binds, connects with the receiver and then just closes the socket,
without ever sending anything.

## How to test

- start the receiver
- start sender multiple times

Notice the receiver patiently waits.

## Conclusion

The receiver never times out or errors out, it just sits quietly until a proper
sender will provide him with some data.
