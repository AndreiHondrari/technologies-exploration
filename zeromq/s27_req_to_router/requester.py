import random
import itertools as itls

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Requester [{UID}] started")

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)

    counter = itls.count(start=1)

    try:
        sock.connect("tcp://127.0.0.1:7777")

        print(f"[{UID}] Start sending requests")
        while True:
            # request
            msg_value = next(counter)
            msg = f"{UID}_{msg_value}"
            print(f"REQ {msg}")
            sock.send_string(msg)

            # reply
            reply = sock.recv_string()
            print(f"RECV {reply}")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        sock.close(1)

    print("Closing context ...")
    ctx.term()

    print(f"Requester [{UID}] terminated")


if __name__ == '__main__':
    main()
