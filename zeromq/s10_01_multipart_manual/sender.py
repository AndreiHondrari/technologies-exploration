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
            sock.send_string(msg[0], zmq.SNDMORE)
            sock.send_string(msg[1], zmq.SNDMORE)
            sock.send_string(msg[2])

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nSender terminated")
