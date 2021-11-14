import zmq


def main() -> None:
    print("Start proxy")
    ctx = zmq.Context()

    requesters = ctx.socket(zmq.ROUTER)
    requesters.bind("tcp://*:5555")

    repliers = ctx.socket(zmq.DEALER)
    repliers.bind("tcp://*:6666")

    try:
        zmq.proxy(requesters, repliers)
    except KeyboardInterrupt:
        print("\nKill detected")
    finally:
        print("Cleaning ...")
        requesters.close(1000)
        repliers.close(1000)
        ctx.term()


if __name__ == '__main__':
    main()
