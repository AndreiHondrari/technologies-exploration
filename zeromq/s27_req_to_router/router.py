import argparse
import time
import itertools as itls

from typing import Set

import zmq


def main() -> None:
    print("ROUTER START")
    ctx = zmq.Context()

    router = ctx.socket(zmq.ROUTER)

    print("Register polling")
    poller = zmq.Poller()
    poller.register(router, zmq.POLLIN)

    counter = itls.count(start=1)

    try:
        router.bind("tcp://127.0.0.1:7777")

        # This is technically a bad way to do it and
        # a better way to wait for all the requesters to connect
        # would be by making a node coordination scheme.
        # this is just for demonstration purposes
        WAIT_TIME = 2
        print(f"Wait {WAIT_TIME}s for requesters to connect ...")
        time.sleep(WAIT_TIME)

        print("Main execution ...")
        requesters: Set[bytes] = set()

        while True:
            polled = dict(poller.poll(1000))

            if len(polled) == 0:
                print("Nothing else to be polled")
                break

            parts = router.recv_multipart()
            requester_address = parts[0]
            # parts[1] will be the empty delimiter frame of the request
            requester_msg = parts[2]

            print(f"RECV [{requester_address}] {requester_msg.decode()}")
            requesters.add(requester_address)

        print("Responding to all requesters ...")
        for address in requesters:
            reply_value = next(counter)
            reply = str(reply_value).encode()
            print(f"REP {reply_value}")
            router.send_multipart([address, b'', reply])

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        router.close(1)

    print("Terminating context ...")
    ctx.term()

    print("ROUTER END")


if __name__ == '__main__':
    main()
