import time

from random import randint
from typing import Any

import zmq


DEALER_ROUTING_ID = b'\x00\x00\x00\x01'


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"DEALER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    routers = ctx.socket(zmq.DEALER)  # type: ignore

    routers.setsockopt(zmq.ROUTING_ID, DEALER_ROUTING_ID)

    try:
        routers.bind("tcp://127.0.0.1:7777")

        while True:
            msg = routers.recv_string()
            tprint("RECV", msg)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        routers.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"DEALER [{UID}] STOP")


if __name__ == "__main__":
    main()
