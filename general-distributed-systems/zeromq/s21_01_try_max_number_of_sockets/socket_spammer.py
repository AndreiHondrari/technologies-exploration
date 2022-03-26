import time
import argparse

import multiprocessing as mp

import zmq


def spam(index: int) -> None:
    print(f"[SPAM BOT {index:0>3}] START")
    ctx = zmq.Context()

    sockets = []

    i = 1

    try:
        while True:
            try:
                print(f"[SPAM BOT {index:0>3}] SOCKET {i}")
                new_socket = ctx.socket(zmq.PUSH)
                sockets.append(new_socket)
                new_socket.connect("tcp://127.0.0.1:5555")
                i += 1

            except zmq.ZMQError as zerr:
                print(repr(zerr))
                break

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n[SPAM BOT {index:0>3}] SIGINT detected")

    print(f"[SPAM BOT {index:0>3}] Cleaning ...")
    for s in sockets:
        s.close(0)

    ctx.term()

    print(f"[SPAM BOT {index:0>3}] STOP")


def main() -> None:
    print("SPAMMER SPAWNER START")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'spammers_count',
        type=int,
        help="Number of spammers to spawn",
        default=1,
    )
    args = parser.parse_args()

    # create spammers
    spammers = []
    for i in range(1, args.spammers_count + 1):
        new_spammer = mp.Process(target=spam, args=(i,))
        spammers.append(new_spammer)

    try:
        # start spammers
        for s in spammers:
            s.start()

        # join spammers
        for s in spammers:
            s.join()

    except KeyboardInterrupt:
        print("\n[SPAWNER] Ctrl+C detected")
    finally:
        print("[SPAWNER] Waiting spammers to halt ...")
        for s in spammers:
            s.join()

    print("SPAMMER SPAWNER STOP")


if __name__ == "__main__":
    main()
