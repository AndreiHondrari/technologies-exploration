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
    dealers = ctx.socket(zmq.ROUTER)  # type: ignore

    try:
        dealers.bind("tcp://127.0.0.1:7777")

        CONN_WAIT_TIME = 1
        tprint(f"Wait {CONN_WAIT_TIME}s for other nodes to connect ...")
        time.sleep(CONN_WAIT_TIME)

        tprint("Start receiveing ...")
        while True:
            parts = dealers.recv_multipart()
            tprint("RECV", parts)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        dealers.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"ROUTER [{UID}] STOP")


if __name__ == "__main__":
    main()
