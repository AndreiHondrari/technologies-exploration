import argparse
import time
import itertools as itls

import zmq


def main(iterations_amount: int) -> None:
    print("DEALER START")
    print(f"Amount of iterations to do: {iterations_amount}")
    ctx = zmq.Context()

    dealer = ctx.socket(zmq.DEALER)

    dealer_rcvhwm = dealer.getsockopt(zmq.RCVHWM)
    print("RCVHWM:", dealer_rcvhwm)

    print("Register polling")
    poller = zmq.Poller()
    poller.register(dealer, zmq.POLLIN)

    counter = itls.count(start=1)

    try:
        dealer.bind("tcp://127.0.0.1:7777")

        # This is technically a bad way to do it and
        # a better way to wait for all the repliers to connect
        # would be by making a node coordination scheme.
        # this is just for demonstration purposes
        WAIT_TIME = 2
        print(f"Wait {WAIT_TIME}s for repliers to connect ...")
        time.sleep(WAIT_TIME)

        print("Main execution ...")

        for i in range(iterations_amount):
            msg = str(next(counter)).encode()
            print("SND", msg, flush=True)
            dealer.send_multipart([b'', msg])

        last_part = None
        for i in range(iterations_amount):
            polled = dict(poller.poll(1000))

            if len(polled) == 0:
                print(
                    f"Abnormal poll-timeout at recv iteration # {i}",
                    flush=True
                )

            try:
                parts = dealer.recv_multipart(zmq.DONTWAIT)
                last_part = parts
                print("RECV", parts, flush=True)
            except zmq.Again:
                print("Apparently there are no more messages in the buffer")
                break

        print(i, last_part)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        dealer.close(1)

    print("Terminating context ...")
    ctx.term()

    print("DEALER END")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        type=int,
        dest='iterations_amount',
        help='The amount of times it should send and receive',
        default=5
    )
    args = parser.parse_args()

    main(args.iterations_amount)
