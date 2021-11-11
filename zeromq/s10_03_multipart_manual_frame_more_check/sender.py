import time
import random
import string

import zmq


if __name__ == '__main__':
    print("Starting sender ...")

    print("Acquiring socket ...")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)
    sock.connect("tcp://localhost:5555")

    print("Start sending ...")
    try:
        while True:
            msg = (
                "".join(random.sample(string.ascii_lowercase, 3)),
                "".join(random.sample(string.ascii_lowercase, 3)),
                "".join(random.sample(string.ascii_lowercase, 3)),
            )
            print("Sending", msg, flush=True)

            msg_parts = tuple(
                map(
                    lambda s: s.encode(),
                    msg
                )
            )
            sock.send_multipart(msg_parts, zmq.DONTWAIT)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSender terminated")
