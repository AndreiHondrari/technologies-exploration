import zmq


def main() -> None:
    print("Broker started")
    ctx = zmq.Context()

    router = ctx.socket(zmq.ROUTER)
    router.bind("tcp://*:5555")

    dealer = ctx.socket(zmq.DEALER)
    dealer.bind("tcp://*:7777")

    zmq.proxy(router, dealer)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nBroker terminated")
