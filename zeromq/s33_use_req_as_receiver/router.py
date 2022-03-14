import time
import copy

from random import randint, random
from typing import Any, Set

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"ROUTER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    workers = ctx.socket(zmq.ROUTER)  # type: ignore

    workers.setsockopt(zmq.ROUTER_MANDATORY, True)
    workers.setsockopt(zmq.ROUTER_HANDOVER, True)

    poller = zmq.Poller()  # type: ignore
    poller.register(workers, zmq.POLLIN)

    worker_address_set: Set[bytes] = set()

    try:
        workers.bind("tcp://127.0.0.1:7777")

        while True:
            # recv sequence
            while True:
                polled = dict(poller.poll(0))

                if len(polled) == 0:
                    break

                if workers in polled:
                    address, _, message = workers.recv_multipart()

                    # register newly connected worker
                    if message == b"READY":
                        tprint(f"Registering {address}")
                        worker_address_set.add(address)

                    # handle
                    else:
                        tprint("RECV", message.decode())

            # send sequence
            temporary_address_set = copy.copy(worker_address_set)
            for w_address in temporary_address_set:
                try:
                    msg = str(randint(100, 1_000))
                    tprint(f"SND TO {str(w_address)}", msg)
                    workers.send_multipart([w_address, b'', msg.encode()])

                except zmq.ZMQError as zerr:
                    if zerr.errno != zmq.EHOSTUNREACH:
                        raise zerr

                    tprint(f" {str(w_address)} Unreachable. ")

                tprint(f"Deregistering {str(w_address)}...")
                worker_address_set.remove(w_address)

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        workers.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"ROUTER [{UID}] STOP")


if __name__ == "__main__":
    main()
