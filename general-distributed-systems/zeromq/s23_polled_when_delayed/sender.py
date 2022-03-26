import time
import random
import string

from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    tprint("[SENDER] START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    try:
        sock.connect("tcp://127.0.0.1:5678")

        while True:
            msg = "".join(random.sample(string.ascii_letters, 10))
            tprint(f"[SENDER] SND {msg}", end="", flush=True)
            sock.send_string(msg)
            print(" DONE", flush=True)

            time.sleep(0.4)

    except KeyboardInterrupt:
        print("\nCtrl+C detected", flush=True)
    finally:
        tprint("[SENDER] Closing socket ...", flush=True)
        sock.close(10)

        tprint("[SENDER] Terminating context ...", flush=True)
        ctx.term()

    tprint("[SENDER] STOP", flush=True)


if __name__ == "__main__":
    main()
