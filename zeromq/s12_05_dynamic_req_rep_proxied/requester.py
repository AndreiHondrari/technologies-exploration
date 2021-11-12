import random
import time

import zmq


def main(UID: int) -> None:
    print(f"Requester [{UID}] started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect("tcp://localhost:5555")

    print(f"[{UID}] Start sending requests")
    while True:
        # request
        when = time.strftime("%M:%S")
        msg = f"'{UID}' -> {random.randint(100, 1000)}"
        print(f"[{UID}] [{when}] SND", msg)
        sock.send_string(msg)

        # reply
        reply = sock.recv_string()
        when = time.strftime("%M:%S")
        print(f"[{UID}] [{when}] REPL", reply)
        time.sleep(random.randint(1, 3))

    sock.close()


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    try:
        main(UID)
    except KeyboardInterrupt:
        print(f"\nRequester [{UID}] terminated")
