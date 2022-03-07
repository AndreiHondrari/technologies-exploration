import random
import time

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Requester [{UID}] started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect("tcp://localhost:5555")

    print(f"[{UID}] Start sending requests")
    try:
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
    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()

    print(f"\nRequester [{UID}] terminated")


if __name__ == '__main__':
    main()
