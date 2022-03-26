import argparse
import time

from random import randint, random
from typing import Any

import zmq


DEALER_A_ROUTING_ID = b'\x01'
DEALER_B_ROUTING_ID = b'\x02'


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main(is_router_handover_enabled: bool) -> None:
    UID = randint(1000, 10_000)
    tprint(f"ROUTER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    dealers = ctx.socket(zmq.ROUTER)  # type: ignore

    dealers.setsockopt(zmq.ROUTER_HANDOVER, is_router_handover_enabled)
    dealers.setsockopt(zmq.ROUTER_MANDATORY, True)

    try:
        dealers.bind("tcp://127.0.0.1:7777")

        CONN_WAIT_TIME = 1
        tprint(f"Wait {CONN_WAIT_TIME}s for other nodes to connect ...")
        time.sleep(CONN_WAIT_TIME)

        while True:
            # for dealer A
            try:
                msg = str(randint(100, 1_000))
                tprint("SND TO A", msg)
                dealers.send_multipart([DEALER_A_ROUTING_ID, msg.encode()])

            except zmq.ZMQError as zerr:
                if zerr.errno != zmq.EHOSTUNREACH:
                    raise zerr

                print("A UNREACHABLE")

            # for dealer B
            try:
                msg = str(randint(100, 1_000))
                tprint("SND TO B", msg)
                dealers.send_multipart([DEALER_B_ROUTING_ID, msg.encode()])

            except zmq.ZMQError as zerr:
                if zerr.errno != zmq.EHOSTUNREACH:
                    raise zerr

                print("B UNREACHABLE")

            time.sleep(0.3 + 0.7 * random())

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        dealers.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"ROUTER [{UID}] STOP")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-rh',
        help="Router handover enabled",
        action='store_true',
        dest='router_handover',
    )
    args = parser.parse_args()
    main(args.router_handover)
