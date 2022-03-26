import random
import time

import zmq


def main(UID: int) -> None:
    print(f"Subscriber [{UID}] started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.connect("tcp://localhost:7777")
    sock.setsockopt(zmq.SUBSCRIBE, b'')

    print(f"[{UID}] Start receiving")
    while True:
        msg = sock.recv_string()
        when = time.strftime("%M:%S")
        print(f"[{UID}] [{when}] RECV", msg)


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    try:
        main(UID)
    except KeyboardInterrupt:
        print(f"\nSubscriber [{UID}] terminated")
