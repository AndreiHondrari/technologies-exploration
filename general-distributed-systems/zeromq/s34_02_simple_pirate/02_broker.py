import time

from random import randint
from typing import Any, List

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"ROUTER [{UID}] START")

    ctx = zmq.Context()  # type: ignore

    requesters = ctx.socket(zmq.ROUTER)  # type: ignore
    workers = ctx.socket(zmq.ROUTER)  # type: ignore

    # requesters.setsockopt(zmq.ROUTER_MANDATORY, True)
    requesters.setsockopt(zmq.ROUTER_HANDOVER, True)

    # workers.setsockopt(zmq.ROUTER_MANDATORY, True)
    workers.setsockopt(zmq.ROUTER_HANDOVER, True)

    poller = zmq.Poller()  # type: ignore
    poller.register(requesters, zmq.POLLIN)
    poller.register(workers, zmq.POLLIN)

    workers_address_list: List[bytes] = []

    try:
        requesters.bind("tcp://127.0.0.1:7777")
        workers.bind("tcp://127.0.0.1:9999")

        while True:
            polled = dict(poller.poll(0))

            if workers in polled:
                worker_msg_parts = workers.recv_multipart()

                # handle regular READY signal
                # (rep address, empty, message)
                if (
                    len(worker_msg_parts) == 3 and
                    worker_msg_parts[2] == b'READY'
                ):
                    w_address = worker_msg_parts[0]
                    tprint(f"CHECK_IN {str(w_address)}")
                    workers_address_list.append(w_address)

                # handle regular reply
                # (rep address, b'', req_address, reply)
                elif len(worker_msg_parts) == 5:
                    w_address, _, req_address, _, reply = worker_msg_parts
                    workers_address_list.append(w_address)
                    tprint(f"REPLY FROM {str(w_address)} : {reply.decode()}")
                    tprint(f"RESPOND TO {str(req_address)}")
                    requesters.send_multipart([req_address, b'', reply])

                # explain malformation
                else:
                    tprint(f"Malformed message from {worker_msg_parts[0]}")
                    tprint("MALFORMED_BODY", worker_msg_parts)

            if requesters in polled:
                request_parts = requesters.recv_multipart()
                tprint("REQ", request_parts)
                if len(workers_address_list) > 0:
                    worker_address = workers_address_list.pop(0)
                    tprint(f"PASS REQ TO {str(worker_address)}")
                    workers.send_multipart(
                        [worker_address, b'', *request_parts]
                    )
                else:
                    tprint("NO_WORKERS_AVAILABLE")

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    finally:
        tprint("Closing socket ...")
        requesters.close(1)
        workers.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"ROUTER [{UID}] STOP")


if __name__ == "__main__":
    main()
