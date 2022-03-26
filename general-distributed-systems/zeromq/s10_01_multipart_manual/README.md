# Manual multipart

## Overview

The receiver binds and waits for a new message. When a new message is in the
buffer, our receiver will notice it via the poller and then will start receiving
the frame, checking for each frame the `more` attribute, which tells us if the
multipart message is ending or not. When the receiver hits `zmq.Again` it means
that the buffer has been emptied of frames and will now proceed to poll again
for new messages.

The sender(s) connect to the receiver and attempt to send a multipart message by
using the SNDMORE flag with the send function, always sending the last part
without the flag.

## How to test

- start the receiver
- start the sender (or multiple senders)

## Observation

A message is passed on the wire only when the last part of a multipart message
is sent with `socket.send`.

Notice that the receiver will wait for messages to reach it. When a message
reaches its buffers, the poller will notice and it will continue to the
processing part where each multipart message is unloaded from the buffer frame
by frame, looking each time if the frame is the last frame of a given multipart
message, in which case the message is considered whole.

When there are no more messages in the buffer, the receiver proceeds to polling
again.

## Warning

Handling frames like this could read to errors in handling separate multipart
messages.

## When to use this

When you want to have fine control over how a multipart message is handled,
frame by frame.

## Some examples

- post processing of multipart frames as they are received, instead of just
  receiving everything and doing post processing. Especially useful for large
  multipart messages (like files)
