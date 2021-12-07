import zmq


def main() -> None:
    print("Start advertiser")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PAIR)
    sock.bind("ipc://gandalf")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    print("Listening ...")
    try:
        while True:
            poller.poll()
            msg = sock.recv_string()
            print(msg, flush=True)
    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print("Cleaning ....")
        sock.close()
        ctx.term()

    print("Stop advertiser")


if __name__ == '__main__':
    main()
