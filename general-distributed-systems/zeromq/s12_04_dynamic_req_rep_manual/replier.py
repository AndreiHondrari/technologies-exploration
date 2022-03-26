import random
import time

import zmq


def main(UID: int) -> None:
    print(f"Replier [{UID}] started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.connect("tcp://localhost:7777")

    print(f"[{UID}] Start listening for requests")
    while True:
        # request
        request = sock.recv_string()
        when = time.strftime("%M:%S")
        print(f"[{UID}] [{when}] RECV", request)

        # reply
        reply = f"[{UID}] Roger for | {request} |"
        print(f"[{UID}] [{when}] REPL", reply)
        sock.send_string(reply)


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    try:
        main(UID)
    except KeyboardInterrupt:
        print(f"\nReplier [{UID}] terminated")
