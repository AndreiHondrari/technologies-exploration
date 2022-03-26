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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        dest='spammers_count',
        type=int,
        help="Number of spammers to spawn",
        default=1,
    )
    parser.add_argument(
        '-s',
        dest='sockets_amount',
        type=int,
        help="Number of sockets to create per bot",
        default=1,
    )
    parser.add_argument(
        '-e',
        dest='eager_close',
        action='store_true',
        # type=bool,
        help="If sockets should close immediately after send",
    )
    args = parser.parse_args()

    accumulation_queue = mp.Queue()

    # create spammers
    spammers = []
    for i in range(1, args.spammers_count + 1):
        new_spammer = mp.Process(
            target=spam,
            args=(
                i,
                args.sockets_amount,
                accumulation_queue,
                args.eager_close,
            )
        )
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
            s.join(10)
            if s.is_alive():
                print("KILL")
                s.kill()

    total = 0
    while not accumulation_queue.empty():
        val = accumulation_queue.get()
        print(f"MSG COUNT: {val}")
        total += val

    print(f"TOTAL MESSAGES SENT: {total}")

    print("SPAMMER SPAWNER STOP")


if __name__ == "__main__":
    main()
