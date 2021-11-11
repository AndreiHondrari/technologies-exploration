from typing import Optional

import zmq

if __name__ == '__main__':
    print("Starting reader ...")
    ctx = zmq.Context()

    print("Acquiring sockets")
    sender1_sock = ctx.socket(zmq.PULL)
    sender1_sock.connect("tcp://localhost:5551")

    sender2_sock = ctx.socket(zmq.PULL)
    sender2_sock.connect("tcp://localhost:5552")

    print("Start reading")
    try:
        while True:
            # SENDER 1
            msg1: Optional[str] = None
            while True:
                try:
                    msg1 = sender1_sock.recv_string(flags=zmq.DONTWAIT)
                except zmq.Again:
                    break

            if msg1 is not None:
                print("S1", msg1)

            # SENDER 2
            msg2: Optional[str] = None
            while True:
                try:
                    msg2 = sender2_sock.recv_string(flags=zmq.DONTWAIT)
                except zmq.Again:
                    break

            if msg2 is not None:
                print("S2", msg2)

    except KeyboardInterrupt:
        print("\nREADER DONE")
