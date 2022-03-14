
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
    tprint(f"DEALER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    routers = ctx.socket(zmq.DEALER)  # type: ignore

    try:
        routers.bind("tcp://127.0.0.1:7777")

        CONN_WAIT_TIME = 1
        tprint(f"Wait {CONN_WAIT_TIME}s for other nodes to connect ...")
        time.sleep(CONN_WAIT_TIME)

        i = 1
        while True:
            msg = str(i)
            tprint("SND", msg)
            routers.send_string(msg)
            i += 1
            time.sleep(0.3 + 0.7 * random())

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
