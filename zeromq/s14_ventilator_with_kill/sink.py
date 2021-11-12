import random
import time

import zmq


def main() -> None:
    print("Sink started")
    ctx = zmq.Context()

    sink_sock = ctx.socket(zmq.PULL)
    sink_sock.bind("tcp://*:6666")

    kill_sock = ctx.socket(zmq.PUB)
    kill_sock.bind("tcp://*:8888")

    print("Obtaining tasks count ...")
    tasks_count_sock = ctx.socket(zmq.PULL)
    tasks_count_sock.bind("tcp://*:7777")
    NO_OF_TASKS: int = tasks_count_sock.recv_pyobj()
    tasks_count_sock.close()
    print("Tasks count", NO_OF_TASKS)

    print("Collecting results ...")
    try:
        for i in range(NO_OF_TASKS):
            result = sink_sock.recv_pyobj()
            print("RECV", result, flush=True)
    except KeyboardInterrupt:
        print(f"\nSink terminated")
    finally:
        print("Cleaning ...")
        kill_sock.send(b'')
        sink_sock.close()
        kill_sock.close()
        ctx.term()


if __name__ == '__main__':
    main()
