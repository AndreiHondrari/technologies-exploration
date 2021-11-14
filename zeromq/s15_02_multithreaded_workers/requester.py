import random
import time
import threading

from typing import Optional

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Requester [{UID}] started")

    ctx = zmq.Context()
    service = ctx.socket(zmq.REQ)
    service.connect("tcp://localhost:5555")

    poller = zmq.Poller()
    poller.register(service, zmq.POLLIN)

    print("Sending requests ...")
    try:
        bla = 0
        while True:
            # request
            if bla == 0:
                msg = str(random.randint(100, 1000))
                print(f"[{UID}] SND", msg)
                service.send_string(msg)
                bla = 1

            polled = dict(poller.poll(1000))

            if len(polled) == 0:
                print(f"{UID} NOTHING POLLED")
                break

            # reply
            if bla == 1:
                if service in polled:
                    reply: Optional[str] = service.recv_string()
                    print(f"[{UID}] REPL", reply)
                    bla = 0
                else:
                    print("SKIP")

            time.sleep(random.random() / 10)

    except KeyboardInterrupt:
        print(f"\n[{UID}] Stop detected")
    finally:
        print(f"[{UID}] Cleaning ...")
        poller.unregister(service)
        service.close(0)
        ctx.term()

    print(f"Requester [{UID}] terminated")


if __name__ == '__main__':
    main()
