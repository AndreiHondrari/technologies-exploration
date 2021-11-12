import random
import time

import zmq


def main(UID: int) -> None:
    print(f"Publisher [{UID}] started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect("tcp://localhost:5555")

    print(f"[{UID}] Start sending")
    while True:
        when = time.strftime("%M:%S")
        msg = f"'{UID}' -> {random.randint(100, 1000)}"
        print(f"[{UID}] [{when}] SND", msg)
        sock.send_string(msg)
        time.sleep(1)

    sock.close()


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    try:
        main(UID)
    except KeyboardInterrupt:
        print(f"\nPublisher [{UID}] terminated")
