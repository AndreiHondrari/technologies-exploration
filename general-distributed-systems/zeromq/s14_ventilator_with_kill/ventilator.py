import random
import time

import zmq


def main() -> None:
    print("Ventilator started")
    ctx = zmq.Context()

    ventilator_sock = ctx.socket(zmq.PUSH)
    ventilator_sock.bind("tcp://*:5555")

    NO_OF_TASKS = 20
    print("Sending tasks count ...")
    tasks_count_sock = ctx.socket(zmq.PUSH)
    tasks_count_sock.connect("tcp://localhost:7777")
    tasks_count_sock.send_pyobj(NO_OF_TASKS)
    tasks_count_sock.close()

    print("Sending tasks")
    try:
        for i in range(NO_OF_TASKS):
            val = random.randint(100, 1000)
            print("SND", val, flush=True)
            ventilator_sock.send_pyobj(val)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nVentilator terminated")
    finally:
        print("Cleaning ...")
        ventilator_sock.close()
        ctx.term()


if __name__ == '__main__':
    main()
