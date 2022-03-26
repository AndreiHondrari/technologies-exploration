
import time

from random import randint
from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


TIME_BETWEEN_REQUESTS = 3
NO_OF_RETRIES = 3
REPLY_TIMEOUT = 1000  # milliseconds


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"NODE [{UID}] START")

    ctx = zmq.Context()  # type: ignore

    poller = zmq.Poller()  # type: ignore

    msg = ''

    try:
        is_recycle = False

        # recycle socket loop
        while True:
            socket = ctx.socket(zmq.REQ)  # type: ignore
            socket.setsockopt_string(zmq.ROUTING_ID, str(UID))
            poller.register(socket)
            socket.connect("tcp://127.0.0.1:7777")

            is_good = True
            while is_good:
                # select a message
                if not is_recycle:
                    print("SELECT NEW MESSAGE")
                    msg = str(randint(100, 1_000))

                # make sure to select a new message next time
                is_recycle = False

                # send the message
                tprint("SND", msg)
                socket.send_string(msg)

                # retry loop
                is_good = False
                for i in range(NO_OF_RETRIES):
                    polled = dict(poller.poll(REPLY_TIMEOUT))

                    if len(polled) == 0:
                        print("RETRY TO RECV")
                        continue

                    if socket in polled:
                        is_good = True
                        reply = socket.recv_string()
                        tprint("RECV", reply)
                        break

                if is_good:
                    time.sleep(TIME_BETWEEN_REQUESTS)

            # recycle socket
            poller.unregister(socket)  # type: ignore
            socket.close(1)
            is_recycle = True
            tprint("RECYCLE")

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
