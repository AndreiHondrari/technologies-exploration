
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
    tprint(f"NODE [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    socket = ctx.socket(zmq.DEALER)  # type: ignore

    try:
        socket.bind("tcp://127.0.0.1:7777")

        while True:
            msg = socket.recv_string()
            tprint("RECV", msg)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        socket.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"NODE [{UID}] STOP")


if __name__ == "__main__":
    main()
