import random

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Requester {UID} started")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)

    try:
        print(f"[{UID}] Connect ...")
        sock.connect("tcp://127.0.0.1:5555")
        print(f"[{UID}] CONNECTED !")

        # request
        msg = str(random.randint(100, 1000))
        print(f"[{UID}] SND {msg}")
        sock.send_string(msg)

        # reply
        reply = sock.recv_string()
        print(f"[{UID}] RCV {reply}")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print(f"[{UID}] Closing socket ...")
        sock.close(1)

    print(f"[{UID}] Closing context ...")
    ctx.term()

    print(f"Requester {UID} dead")


if __name__ == '__main__':
    main()
