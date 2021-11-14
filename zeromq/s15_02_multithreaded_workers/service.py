import random
import time
import threading

import zmq


def do_work(
    kill_event: threading.Event,
    ctx: zmq.Context,
    url_workers: str
):
    WORKER_ID = random.randint(1000, 10_000)
    print(f"Worker [{WORKER_ID}] started")
    worker_sock = ctx.socket(zmq.REP)
    worker_sock.connect(url_workers)

    poller = zmq.Poller()
    poller.register(worker_sock, zmq.POLLIN)

    while not kill_event.is_set():
        polled = dict(poller.poll(1000))
        if worker_sock in polled:
            message = worker_sock.recv_string()
            if message is not None:
                print(f"W[{WORKER_ID}] RECV", message, flush=True)
                reply = f"[{WORKER_ID}] {message} received"
                print(f"W[{WORKER_ID}] REPL FOR {message}", flush=True)
                worker_sock.send_string(reply)
        else:
            print(f"[{WORKER_ID}] SKIP")

    print(f"W[{WORKER_ID}] closing socket ...")
    worker_sock.close()
    print(f"Worker [{WORKER_ID}] terminated")


def main() -> None:
    print("Start service")
    URL_CLIENTS = "tcp://*:5555"
    URL_WORKERS = "inproc://jobs"

    ctx = zmq.Context()

    clients_sock = ctx.socket(zmq.ROUTER)
    clients_sock.bind(URL_CLIENTS)

    workers_sock = ctx.socket(zmq.DEALER)
    workers_sock.bind(URL_WORKERS)

    kill_event = threading.Event()

    NO_OF_WORKERS = 3
    workers = []
    for i in range(NO_OF_WORKERS):
        workers.append(
            threading.Thread(
                target=do_work,
                args=(kill_event, ctx, URL_WORKERS,)
            )
        )

    try:
        # start the workers
        for worker in workers:
            worker.start()

        # forward requests to workers
        zmq.proxy(clients_sock, workers_sock)
    except KeyboardInterrupt:
        print("\nStop detected")
        # signal workers to die
        kill_event.set()

        # wait for workers to die
        for worker in workers:
            worker.join()

    finally:
        # clean sockets and ctx
        print("Cleaning sockets ...")
        clients_sock.close(0)
        workers_sock.close(0)
        ctx.term()

    print("Service terminated")


if __name__ == '__main__':
    main()
