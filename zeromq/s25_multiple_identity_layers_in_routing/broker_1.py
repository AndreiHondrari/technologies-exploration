import zmq


def main() -> None:
    print("Broker started")
    ctx = zmq.Context()

    router = ctx.socket(zmq.ROUTER)
    router.bind("tcp://127.0.0.1:5555")

    dealer = ctx.socket(zmq.DEALER)
    dealer.connect("tcp://127.0.0.1:6666")

    print("Register polling")
    poller = zmq.Poller()
    poller.register(router, zmq.POLLIN)
    poller.register(dealer, zmq.POLLIN)

    while True:
        # print("Poll")
        polled = dict(poller.poll())

        # requesters to repliers
        if router in polled:
            parts = router.recv_multipart()
            print("\n---\nR -> D")
            for p in parts:
                print(p)
            dealer.send_multipart(parts)

        # repliers to requesters
        if dealer in polled:
            parts = dealer.recv_multipart()
            print("\n---\nD -> R")
            for p in parts:
                print(p)
            router.send_multipart(parts)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nBroker terminated")
