import random
import time

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Replier [{UID}] started")

    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)

    try:
        sock.connect("tcp://127.0.0.1:8888")

        print(f"[{UID}] Start listening for requests")
        while True:
            # request
            request = sock.recv_string()
            when = time.strftime("%M:%S")
            print(f"[{UID}] [{when}] RECV", request)

            # reply
            reply = str(random.randint(1000, 10_000))
            print(f"[{UID}] REP {reply}")
            sock.send_string(reply)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        sock.close(1)

    print("Closing context ...")
    ctx.term()

    print(f"Replier [{UID}] terminated")


if __name__ == '__main__':
    main()
