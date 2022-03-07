import sys
import signal
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
    sock.connect(url_worker)

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    while not kill_event.is_set():
        polled = dict(poller.poll(0.5))
        if sock in polled:
            when = time.strftime("%H:%M:%S")
            print()
            print('-' * 10, when, '-' * 10)

            print("[WORKER] WAIT RECV")
            msg = sock.recv_string()
            print("[WORKER] RECV", msg)

            print("[WORKER] REPLY PONG ...")
            sock.send_string("PONG")
            print("[WORKER] REPLIED")

    sock.close(0)
    print("[WORKER] STOP")


attempted_stop: bool = False


class ReplierExit(Exception):
    pass


def main() -> None:
    print("[MASTER] START")
    ctx = zmq.Context()

    # socks stuff
    URL_WORKER = "inproc://gandalf"

    requesters = ctx.socket(zmq.ROUTER)
    requesters.bind("tcp://*:5555")

    repliers = ctx.socket(zmq.DEALER)
    repliers.bind(URL_WORKER)

    # create thread

    kill_event = threading.Event()
    thread = threading.Thread(
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

        raise ReplierExit

    signal.signal(signal.SIGINT, sigint_handle)

    thread.start()

    # proxy requests to our worker
    try:
        zmq.proxy(requesters, repliers)
    except ReplierExit:
        print("[MASTER] REPLIER EXIT RAISED")

    print("[MASTER] WAIT FOR WORKER THREAD TO FINISH ...")
    thread.join()

    print("[MASTER] Cleaning ...")
    requesters.close(1000)
    repliers.close(1000)
    ctx.term()
    print("[MASTER] Terminated")

    print("[MASTER] STOP")


if __name__ == '__main__':
    main()
