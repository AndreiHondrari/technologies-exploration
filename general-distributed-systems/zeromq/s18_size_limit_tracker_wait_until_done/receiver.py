import time

from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


if __name__ == '__main__':
    tprint("[RECEIVER] START")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://*:5555")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    try:
        while True:
            tprint('-' * 20)
            tprint("Wait for new large message")
            polled = dict(poller.poll())
            tprint("Message received")

            if sock in polled:
                data = sock.recv()
                val = int.from_bytes(data, 'big')
                tprint(f"{len(data)} -> {val}")

    except KeyboardInterrupt:
        tprint("\nStop detected")

    finally:
        sock.close()
        ctx.term()

    tprint("[RECEIVER] STOP")
