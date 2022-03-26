import zmq


def main() -> None:
    print("Proxy started")
    ctx = zmq.Context()

    xsub = ctx.socket(zmq.XSUB)
    xsub.bind("tcp://127.0.0.1:5555")

    xpub = ctx.socket(zmq.XPUB)
    xpub.bind("tcp://127.0.0.1:7777")

    zmq.proxy(xsub, xpub)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProxy terminated")
