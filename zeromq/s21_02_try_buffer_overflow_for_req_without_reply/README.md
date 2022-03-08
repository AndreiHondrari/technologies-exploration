# Spawn many sockets

See how many sockets can ZeroMQ spawn and handle.

## Observations

In a Linux container, the socket count was growing fast, so much that docker
freezed.

On MacOS, a lot of sockets were being spawned, but after a while, in the range
of thousands, the server started recording FAILED handshakes.
