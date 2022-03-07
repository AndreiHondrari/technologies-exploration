import signal
import sys
import time
import threading

from types import FrameType

import zmq


def do_work(
    kill_event: threading.Event,
    ctx: zmq.Context,
    url_worker: str
) -> None:
    print("[WORKER] START")
    sock = ctx.socket(zmq.REP)
    rc = sock.connect(url_worker)
    print("[WORKER] Socket RC:", rc)

    try:
        while not kill_event.is_set():
            when = time.strftime("%H:%M:%S")
            print()
            print('-' * 10, when, '-' * 10)

            print("[WORKER] WAIT RECV")
            msg = sock.recv_string()
            print("[WORKER] RECV", msg)

            print("[WORKER] REPLY PONG ...")
            sock.send_string("PONG")
            print("[WORKER] REPLIED")
    except KeyboardInterrupt:
        print("[WORKER] Caught SIGINT")

    print()
    print("[WORKER]", '-' * 20)
    print("[WORKER] After loop")

    print("[WORKER] Closing ...")
    sock.close()

    print("[WORKER] STOP")


attempted_stop: bool = False


def main() -> None:

    print("[MASTER] START")
    ctx = zmq.Context()

    URL_WORKER = "tcp://localhost:6666"
    kill_event = threading.Event()
    worker_thread = threading.Thread(
        target=do_work,
        args=(kill_event, ctx, URL_WORKER,)
    )

    def sigint_handle(signum: int, frame: FrameType) -> None:
        global attempted_stop

        if attempted_stop:
            print("\n---> Forcefully killing workers and master", flush=True)
            sys.exit()
        else:
            print("\n---> Ctrl+C detected")
            print("---> Shutting down peacefully ...")
            kill_event.set()
            attempted_stop = True

    signal.signal(signal.SIGINT, sigint_handle)

    worker_thread.start()

    worker_thread.join()

    print("[MASTER] Cleaning ...")
    ctx.term()

    print("[MASTER] STOP")


if __name__ == '__main__':
    main()
