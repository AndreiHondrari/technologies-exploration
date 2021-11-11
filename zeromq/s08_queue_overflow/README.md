# Queue overflow

If you constantly send information on a socket and never read from it, the limit of the queue on top of which the socket is built will be eventually reached and then depending on the type of socket (blocking or non-blocking) the function will either halt until the queue is empty or it will throw an error.

## Steps to demonstrate

* run the `empty_queue.py` and keep in mind you have 7 seconds until it will start reading from the socket.
* run the `overflower.py` effectively immediately. It will wait for one second so the socket performs the handshake and then it will send as many messages as it can.

Initial tests show that around 3000-4000 messages will pile up on the queue until a halt or an error happens.
