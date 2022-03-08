import argparse

import multiprocessing as mp

import zmq


def spam(
    index: int,
    sockets_amount: int,
    accumulation_queue: mp.Queue,
    eager_close: bool,
) -> None:
    print(f"[SPAM BOT {index:0>3}] START")
    ctx = zmq.Context()

    sockets = []

    msg_count = 1

    try:
        while True:
            for i in range(sockets_amount):
                try:
                    new_socket = ctx.socket(zmq.REQ)
                    new_socket.connect("tcp://127.0.0.1:5555")
                    sockets.append(new_socket)

                except zmq.ZMQError:
                    break

            for s in sockets:
                s.send(b'-' * 100)
                # s.send(b'-' * 100, zmq.DONTWAIT)
                msg_count += 1
                if eager_close:
                    s.close(1000)
                else:
                    s.close()

            sockets = []

    except KeyboardInterrupt:
        print(f"\n[SPAM BOT {index:0>3}] SIGINT detected")

    print(f"[SPAM BOT {index:0>3}] Report {msg_count} ...")
    accumulation_queue.put(msg_count)

    print(f"[SPAM BOT {index:0>3}] Cleaning ...")
    for s in sockets:
        if not s.closed:
            s.close(0)

    ctx.term()

    print(f"[SPAM BOT {index:0>3}] STOP")


def main() -> None:
    print("SPAMMER SPAWNER START")
    SOCKETS_AMOUNT = 1000

    ctx = zmq.Context()

    sockets = []

    msg_count = 1

    try:
        while True:
            for i in range(SOCKETS_AMOUNT):
                try:
                    new_socket = ctx.socket(zmq.REQ)
                    new_socket.connect("tcp://127.0.0.1:5555")
                    sockets.append(new_socket)

                except zmq.ZMQError as zerr:
                    print(repr(zerr))
                    break

            for s in sockets:
                # s.send(b'-' * 100)
                s.send(b'-' * 100, zmq.DONTWAIT)
                msg_count += 1
                s.close()

            sockets = []

    except KeyboardInterrupt:
        print("\nSIGINT detected")

    print(f"TOTAL MESSAGES SENT: {msg_count}")

    print("Cleaning ...")
    for s in sockets:
        if not s.closed:
            s.close(0)

    print("Closing context ...")
    ctx.term()

    print("SPAMMER SPAWNER STOP")


if __name__ == "__main__":
    main()
