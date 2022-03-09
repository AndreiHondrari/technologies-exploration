import time
import random
import string

from typing import Any

import zmq


class ConnectionNotAcknowledged(Exception):
    pass


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
    NODE_NAME = "".join(random.sample(string.ascii_uppercase, 10))
    tprint(f"[NODE {NODE_NAME}] START")
    ctx = zmq.Context()
    req_sock = ctx.socket(zmq.REQ)
    in_sock = ctx.socket(zmq.PULL)

    poller = zmq.Poller()
    poller.register(req_sock)
    poller.register(in_sock)

    is_connected = False

    try:
        req_sock.connect("tcp://127.0.0.1:5555")
        in_sock.connect("tcp://127.0.0.1:7777")

        # notify service that we want to connect
        req_sock.send_pyobj({
            "kind": REQUEST_CONNECT,
            "name": NODE_NAME,
        })

        reply_msg = req_sock.recv_string()
        if reply_msg != "ACK":
            raise ConnectionNotAcknowledged

        is_connected = True

        # proceed with receiving
        while True:
            polled = dict(poller.poll())

            if in_sock in polled:
                event = in_sock.recv_pyobj()
                if event['kind'] == EVENT_CONNECT:
                    tprint(f"[NODE {NODE_NAME}] {event['name']} connected")

                elif event['kind'] == EVENT_MSG:
                    tprint(f"[NODE {NODE_NAME}] MSG {event['msg']}")

                elif event['kind'] == EVENT_SHUTDOWN:
                    tprint(f"[NODE {NODE_NAME}] Service ended")
                    break

    except ConnectionNotAcknowledged:
        tprint(f"[NODE {NODE_NAME}] Service did not ACK")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

        # notify service that we quit
        if is_connected:
            tprint(f"[NODE {NODE_NAME}] Notifying service of disconnection")

            try:
                req_sock.send_pyobj({
                    "kind": REQUEST_DISCONNECT,
                    "name": NODE_NAME,
                })

            except zmq.ZMQError as zerr:
                print(
                    f"[NODE {NODE_NAME}] disconnect request failed "
                    f"({repr(zerr)})"
                )

    finally:
        tprint(f"[NODE {NODE_NAME}] Closing sockets ...", flush=True)
        req_sock.close(10)
        in_sock.close(10)

        tprint(f"[NODE {NODE_NAME}] Terminating context ...", flush=True)
        ctx.term()

    tprint(f"[NODE {NODE_NAME}] STOP")


if __name__ == "__main__":
    main()
