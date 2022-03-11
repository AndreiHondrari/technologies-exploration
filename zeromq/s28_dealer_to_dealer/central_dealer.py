import time
import random

from collections import namedtuple

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
    print("CENTRAL DEALER START")
    ctx = zmq.Context()

    workers = ctx.socket(zmq.DEALER)

    print("Register polling")
    poller = zmq.Poller()
    poller.register(workers, zmq.POLLIN)

    try:
        workers.bind("tcp://127.0.0.1:7777")

        # This is technically a bad way to do it and
        # a better way to wait for all the repliers to connect
        # would be by making a node coordination scheme.
        # this is just for demonstration purposes
        WAIT_TIME = 2
        print(f"Wait {WAIT_TIME}s for clients to connect ...")
        time.sleep(WAIT_TIME)

        print("Main execution ...")

        # send tasks
        NUMBER_OF_TASKS = 2

        print("Send tasks ...", flush=True)
        for i in range(NUMBER_OF_TASKS):
            # prepare task
            task_id = str(random.randint(1000, 10_000))
            count_magic_value = random.randint(1, 10)
            print(f"SND {task_id} : {count_magic_value}")

            # send task to a worker
            envelope = TaskEnvelope(
                task_id=task_id.encode(),
                magic_number=count_magic_value.to_bytes(4, 'big')
            )
            workers.send_multipart(envelope)

        # wait for results
        print("Wait for results ...", flush=True)
        for i in range(NUMBER_OF_TASKS * 9):
            poller.poll(10_000)

            raw_response = workers.recv_multipart()
            reply = Reply(*raw_response)
            task_id = reply.task_id.decode()
            value = int.from_bytes(reply.value, 'big')
            print(f"RECV {task_id} -> {value}")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Closing socket ...")
        workers.close(1)

    print("Terminating context ...")
    ctx.term()

    print("CENTRAL DEALER END")


if __name__ == '__main__':
    main()
