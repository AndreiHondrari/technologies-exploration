import zmq


def main() -> None:
    print("Start subscriber")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, b'kogaion')
    sock.setsockopt(zmq.SUBSCRIBE, b'baldur')
    sock.connect("ipc://gandalf")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    try:
        while True:
            envelope = sock.recv_multipart()
            print("RECV", envelope, flush=True)

    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()
    print("DONE")


if __name__ == '__main__':
    main()
