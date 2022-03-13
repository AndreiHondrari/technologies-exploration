
import time

from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


CENTRAL_ROUTING_ID = b'\x00\x00\x00\xff'


def main() -> None:
    tprint("CENTRAL ROUTER START")

    ctx = zmq.Context()
    satellites = ctx.socket(zmq.ROUTER)

    # notice we deliberately define an address for
    # this router
    satellites.setsockopt(zmq.ROUTING_ID, CENTRAL_ROUTING_ID)

    try:
        satellites.bind("tcp://127.0.0.1:7777")

        while True:
            parts = satellites.recv_multipart()
            tprint("RECV", parts[0], int.from_bytes(parts[1], 'big'))

    except KeyboardInterrupt:
        tprint("nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        satellites.close(1)

    tprint("Closing context ...")
    ctx.term()

    tprint("CENTRAL ROUTER STOP")


if __name__ == "__main__":
    main()
