import time

from typing import Any

import zmq


def tprint(*args: Any, **kwargs: Any) -> None:
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


if __name__ == '__main__':
    tprint("[SENDER] START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    sock.connect("tcp://localhost:5555")

    tprint("Binary send")
    val = 12345
    data = val.to_bytes(750_000_000, 'big')
    tracker = sock.send(data, copy=False, track=True)
    tprint("ISDONE", tracker.done)
    tprint("PASSED TO SEND")
    tprint("WAIT ...")
    tracker.wait()
    tprint("ISDONE", tracker.done)
    tprint("DONE")

    tprint("[SENDER] STOP")
