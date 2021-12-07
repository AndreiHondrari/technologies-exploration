import time
import random
import string

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Start connecter [{UID}]")

    ctx = zmq.Context()
    sock = ctx.socket(zmq.PAIR)
    sock.connect("ipc://gandalf")

    print(f"[{UID}] sending ...")
    try:
        while True:
            msg = "".join(random.sample(string.ascii_lowercase, 5))
            print(f"[{UID}] SND {msg}", flush=True)
            sock.send_string(f"[{UID}] {msg}")
            time.sleep(random.random())
    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print(f"[{UID}] cleaning ...")
        sock.close(1)
        ctx.term()

    print(f"Connecter [{UID}] stopped")


if __name__ == '__main__':
    main()
