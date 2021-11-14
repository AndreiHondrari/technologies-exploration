import time
import random
import threading

import zmq


def do_send(
    ctx: zmq.Context,
    url: str
) -> None:
    print("SND START")
    sock = ctx.socket(zmq.PAIR)
    sock.connect(url)

    print("SND SND")
    sock.send_string("hey yo !")

    print("SND END")


def do_recv(
    ctx: zmq.Context,
    url: str
) -> None:
    print("RECV START")
    sock = ctx.socket(zmq.PAIR)
    sock.bind(url)

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    print("RECV POLL")
    poller.poll()

    msg = sock.recv_string()
    print("RECV MSG", msg)

    print("RECV END")


def main() -> None:
    URL_SOCKS = "inproc://gandalf"

    ctx = zmq.Context()

    sender = threading.Thread(target=do_send, args=(ctx, URL_SOCKS,))
    receiver = threading.Thread(target=do_recv, args=(ctx, URL_SOCKS,))

    sender.start()
    receiver.start()

    sender.join()
    receiver.join()

    ctx.term()


if __name__ == '__main__':
    main()
