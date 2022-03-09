import time

from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def main() -> None:
    tprint("[RECEIVER] START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    try:
        sock.bind("tcp://127.0.0.1:5678")

        while True:
            polled = dict(poller.poll(0))

            if sock in polled:
                tprint("[RECEIVER] Receiving ...", end="", flush=True)
                msg = sock.recv_string()
                print(f" | -> {msg}", flush=True)

    except KeyboardInterrupt:
        print("\nCtrl+C detected", flush=True)
    finally:
        tprint("[RECEIVER] Closing socket ...", flush=True)
        sock.close(10)

        tprint("[RECEIVER] Terminating context ...", flush=True)
        ctx.term()

    tprint("[RECEIVER] STOP", flush=True)


if __name__ == "__main__":
    main()
