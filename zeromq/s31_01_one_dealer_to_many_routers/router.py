
import time

from random import randint
from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"ROUTER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    dealer = ctx.socket(zmq.ROUTER)  # type: ignore

    try:
        dealer.connect("tcp://127.0.0.1:7777")

        while True:
            parts = dealer.recv_multipart()
            tprint("RECV", parts)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        dealer.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"ROUTER [{UID}] STOP")


if __name__ == "__main__":
    main()
