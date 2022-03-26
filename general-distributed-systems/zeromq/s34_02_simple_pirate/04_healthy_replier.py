
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
    socket = ctx.socket(zmq.REQ)  # type: ignore

    socket.setsockopt_string(zmq.ROUTING_ID, str(UID))

    try:
        socket.connect("tcp://127.0.0.1:9999")

        # let broker we want to receive tasks
        socket.send_string("READY")

        while True:
            # get one task
            req_address, _, msg = socket.recv_multipart()
            msg_decoded = msg.decode()
            tprint("RECV", req_address, msg_decoded)

            time.sleep(0.5)

            # reply
            tprint("REPLY")
            reply = f"PONG_{msg_decoded}"
            socket.send_multipart([req_address, b'', reply.encode()])

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
