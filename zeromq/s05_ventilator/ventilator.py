import random
import time
import zmq

if __name__ == '__main__':
    print(f"Starting ventilator ...")
    context = zmq.Context()

    # advertise a socket for the workers
    print("Advertising ventilator socket ...")
    ventilation_socket = context.socket(zmq.PUSH)
    ventilation_socket.bind("tcp://*:5555")

    print("Wait a bit ...")
    time.sleep(1)

    # start feeding the workers
    NO_OF_TASKS: int = 20
    print("Feeding workers ...")
    for i in range(NO_OF_TASKS):
        task = random.randint(0, 10_000)
        print(f"Feeding {i}: {task}")
        ventilation_socket.send_pyobj(task)

    print("Ventilation finalized")
