import random
import time

import zmq

if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting worker [{UID}]")
    context = zmq.Context()

    # connect to the ventilation socket
    print(f"[{UID}] Connecting to ventilator ...")
    ventilator = context.socket(zmq.PULL)
    ventilator.connect("tcp://localhost:5555")
    print(f"[{UID}] Ventilator connected")

    # connect to the sink
    print(f"[{UID}] Connecting to sink ...")
    sink = context.socket(zmq.PUSH)
    sink.connect("tcp://localhost:5558")
    print(f"[{UID}] Sink connected")

    print(f"[{UID}] Start receiving")
    while True:
        task = ventilator.recv_pyobj()
        print(f"[{UID}] Received task: {task}")
        time.sleep(random.random())
        result = task * 2
        task_result = f"{result} for {task}"
        print(f"Processed: {task_result}")
        sink.send_pyobj(task_result)
