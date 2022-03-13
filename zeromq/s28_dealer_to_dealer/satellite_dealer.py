import time
import random

from collections import namedtuple
from typing import Optional, cast

import zmq


TaskEnvelope = namedtuple(
    'TaskEnvelope',
    ['task_id', 'magic_number']
)

Reply = namedtuple(
    'Reply',
    ['task_id', 'value']
)


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"SATELLITE {UID} DEALER START")
    ctx = zmq.Context()

    central_dealer = ctx.socket(zmq.DEALER)

    print("Register polling")
    poller = zmq.Poller()
    poller.register(central_dealer, zmq.POLLIN)

    try:
        central_dealer.connect("tcp://127.0.0.1:7777")

        print("Main execution ...")

        task_id: Optional[bytes] = None
        special_value: Optional[int] = None

        while True:
            print('\n', '-' * 10, sep='')
            print("New session")
            print("Wait for task ...")
            poller.poll()
            raw_envelope = central_dealer.recv_multipart()
            envelope = TaskEnvelope(*raw_envelope)
            task_id = envelope.task_id
            special_value = int.from_bytes(envelope.magic_number, 'big')
            decoded_task_id = cast(bytes, task_id).decode()
            print(f"RECV {decoded_task_id} : {special_value}")

            for i in range(1, 10):
                special_value *= 2
                print("SND", special_value)

                reply = Reply(
                    task_id=task_id,
                    value=special_value.to_bytes(4, 'big')
                )
                central_dealer.send_multipart(reply)

                time.sleep(0.3 + 0.7 * random.random())

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        central_dealer.close(1)

    print("Terminating context ...")
    ctx.term()

    print(f"SATELLITE {UID} DEALER END")


if __name__ == '__main__':
    main()
