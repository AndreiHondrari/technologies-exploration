import time

from random import randint
from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def run(routing_id: bytes) -> None:
    UID = randint(1000, 10_000)
    tprint(f"DEALER [{UID}] START")
    tprint("ROUTING_ID: ", routing_id)

    ctx = zmq.Context()  # type: ignore
    router = ctx.socket(zmq.DEALER)  # type: ignore

    router.setsockopt(zmq.ROUTING_ID, routing_id)

    try:
        router.connect("tcp://127.0.0.1:7777")

        while True:
            msg = router.recv_string()
            tprint("RECV", msg)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        router.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"DEALER [{UID}] STOP")


def main() -> None:
    print('!' * 20)
    print()

    print("WARNING: This is just a library module")
    print("You want to start dealer_a or dealer_b instead")

    print()
    print('!' * 20)


if __name__ == "__main__":
    main()
