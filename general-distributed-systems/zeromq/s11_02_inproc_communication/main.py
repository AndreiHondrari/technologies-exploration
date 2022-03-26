import time
import random
from threading import Thread, Event

import zmq


def runner1(stop_event: Event, ctx: zmq.Context) -> None:
    print("Runner One Started")
    sock: zmq.Socket = ctx.socket(zmq.PUSH)
    rc = sock.connect("inproc://gandalf")
    print("RC", rc)

    while not stop_event.is_set():
        msg = f"{random.randint(1000, 10_000)}"
        print("Runner One SND", msg, flush=True)
        try:
            sock.send_string(msg, zmq.DONTWAIT)
        except zmq.Again:
            pass

        time.sleep(1)

    sock.close()
    print("Runner One Terminated")


def runner2(stop_event: Event, ctx: zmq.Context) -> None:
    print("Runner Two Started")
    sock: zmq.Socket = ctx.socket(zmq.PULL)
    rc = sock.bind("inproc://gandalf")
    print("RC2", rc)

    while not stop_event.is_set():
        try:
            msg = sock.recv_string(zmq.DONTWAIT)
            print("Runner Two RECV", msg, flush=True)
        except zmq.Again:
            pass

    sock.close()
    print("Runner Two Terminated")


def main() -> None:
    stop_event = Event()
    context = zmq.Context()

    t1 = Thread(target=runner1, args=(stop_event, context,))
    t2 = Thread(target=runner2, args=(stop_event, context,))

    t1.start()
    t2.start()

    try:
        t1.join()
        t2.join()
    except (KeyboardInterrupt, SystemExit,):
        print("\nStop detected")
        stop_event.set()
        t1.join()
        t2.join()


if __name__ == '__main__':
    print("Execution started")
    main()
    print("Finish")
