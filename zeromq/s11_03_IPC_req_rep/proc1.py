import zmq
import time

import random


if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect("ipc://gandalf")

    try:
        while True:
            msg = f"> {random.randint(1000, 10_000)} <"
            print("Sending", msg, flush=True)
            sock.send_pyobj(msg)

            reply = sock.recv_pyobj()
            print("Receiving", reply, flush=True)

            time.sleep(random.random())
    except KeyboardInterrupt:
        print("\nProc 1 interrupted")
