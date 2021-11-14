import zmq


def main() -> None:
    print("Start service")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://*:5678")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    try:
        print("Start polling")
        while True:
            polled = poller.poll()
            print(polled)
    except KeyboardInterrupt:
        print("\nKill detected")
    finally:
        print("Terminated")

    sock.close()
    ctx.term()


if __name__ == '__main__':
    main()
