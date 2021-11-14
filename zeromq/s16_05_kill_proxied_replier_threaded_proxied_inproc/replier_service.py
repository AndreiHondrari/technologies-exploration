import threading

import zmq


def do_work(
    kill_event: threading.Event,
    ctx: zmq.Context,
    url_worker: str
) -> None:
    print("Worker started")
    sock = ctx.socket(zmq.REP)
    sock.connect(url_worker)

    while not kill_event.is_set():
        msg = sock.recv_string()
        print("RECV", msg)
        sock.send_string("PONG")

    sock.close(0)
    print("Worker terminated")


def main() -> None:
    print("Start service")
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

    try:
        thread.start()

        # proxy requests to our worker
        zmq.proxy(requesters, repliers)

    except KeyboardInterrupt:
        print("\nKill detected")
        kill_event.set()
        thread.join()
    finally:
        print("Cleaning ...")
        requesters.close(1000)
        repliers.close(1000)
        ctx.term()
        print("Terminated")

    print("END")


if __name__ == '__main__':
    main()
