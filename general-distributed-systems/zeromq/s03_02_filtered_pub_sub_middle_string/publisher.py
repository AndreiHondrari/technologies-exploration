import time
import random

import zmq


def main() -> None:
    print("Start publisher")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.bind("ipc://gandalf")

    try:
        while True:
            msg = f"kogaion {random.randint(100, 1000)}"
            msg2 = f"{random.randint(100, 1000)} excalibur"
            msg3 = f"baldur {random.randint(100, 1000)}"

            print("SND1", msg, flush=True)
            sock.send_string(msg)

            print("SND2", msg2, flush=True)
            sock.send_string(msg2)

            print("SND3", msg3, flush=True)
            sock.send_string(msg3)

            time.sleep(random.random())

    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()
    print("DONE")


if __name__ == '__main__':
    main()
