import time
import random
import string

from typing import Any, List

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


EVENT_CONNECT = 0
EVENT_SHUTDOWN = 1
EVENT_MSG = 2

REQUEST_CONNECT = 0
REQUEST_DISCONNECT = 1


def main() -> None:
    tprint("SERVICE START")
    ctx = zmq.Context()
    req_sock = ctx.socket(zmq.REP)
    out_sock = ctx.socket(zmq.PUSH)

    poller = zmq.Poller()
    poller.register(req_sock)

    TARGET_CLIENT_COUNT = 2
    client_count = 0
    client_names: List[str] = []

    try:
        req_sock.bind("tcp://127.0.0.1:5555")
        out_sock.bind("tcp://127.0.0.1:7777")

        while True:

            print()
            tprint('-' * 20)
            tprint("Preparing new session ...")

            # wait for target clients to connect
            tprint(f"Wait for {TARGET_CLIENT_COUNT} clients to connect ...")
            while True:
                poller.poll()
                request = req_sock.recv_pyobj()

                if request['kind'] == REQUEST_CONNECT:
                    client_count += 1
                    client_names.append(request['name'])
                    req_sock.send_string("ACK")
                    tprint(
                        f"{request['name']} connected "
                        f"({client_count} clients)"
                    )

                elif request['kind'] == REQUEST_DISCONNECT:
                    client_count -= 1
                    client_names.remove(request['name'])

                    try:
                        req_sock.send_string("ACK", zmq.DONTWAIT)
                    except zmq.Again:
                        pass

                    tprint(
                        f"{request['name']} disconnected "
                        f"({client_count} clients)"
                    )

                if client_count >= TARGET_CLIENT_COUNT:
                    tprint("Target client count reached")
                    break

            tprint("Starting session")
            for name in client_names:
                out_sock.send_pyobj({
                    "kind": EVENT_CONNECT,
                    "name": name,
                })

            # secondary main loop
            tprint("Distributing messages ...")
            while True:
                # check if new events from clients
                polled = dict(poller.poll(0))

                if req_sock in polled:
                    request = req_sock.recv_pyobj()
                    if request['kind'] == REQUEST_DISCONNECT:
                        tprint("One client disconnected ...")
                        try:
                            req_sock.send_string("ACK", zmq.DONTWAIT)
                        except zmq.Again:
                            pass

                        break

                # distribute data to clients
                msg = "".join(random.sample(string.ascii_letters, 10))
                tprint(f"SND {msg}")
                out_sock.send_pyobj({
                    "kind": EVENT_MSG,
                    "msg": msg,
                })

                time.sleep(0.5)

            tprint("Closing session ...")
            out_sock.send_pyobj({
                "kind": EVENT_SHUTDOWN
            })

            client_count = 0
            client_names = []

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        tprint("Closing sockets ...", flush=True)
        req_sock.close(10)
        out_sock.close(10)

        tprint("Terminating context ...", flush=True)
        ctx.term()

    tprint("SERVICE STOP")


if __name__ == "__main__":
    main()
