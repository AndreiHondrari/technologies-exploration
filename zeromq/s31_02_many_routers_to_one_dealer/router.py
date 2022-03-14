import time

from random import randint, random
from typing import Any

import zmq


DEALER_ROUTING_ID = b'\x00\x00\x00\x01'


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
            msg = str(randint(100, 1_000))
            tprint("SND", msg)
            dealer.send_multipart([DEALER_ROUTING_ID, msg.encode()])
            time.sleep(0.3 + 0.7 * random())

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
