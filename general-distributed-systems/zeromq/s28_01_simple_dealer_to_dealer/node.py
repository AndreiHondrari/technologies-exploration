
import time

from random import randint, random
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
        socket.connect("tcp://127.0.0.1:7777")

        while True:
            msg = str(randint(100, 1_000))
            tprint("SND", msg)
            socket.send_string(msg)
            time.sleep(0.3 + random() * 0.7)

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
