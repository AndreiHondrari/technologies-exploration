import random
import time
import zmq

if __name__ == '__main__':
    print("Starting ventilator ...")
    context = zmq.Context()

    # advertise a socket for the workers
    print("Advertising ventilator socket ...")
    ventilation_socket = context.socket(zmq.PUSH)
    ventilation_socket.bind("tcp://*:5555")

    try:
        # the reason for waiting is that
        # the ventilator needs to connect
        # to all workers properly
        # before sending,
        # otherwise the round-robin
        # will not complete
        # and all load goes to the first worker
        # to fully do the handshake
        print("Wait a bit ...")
        time.sleep(1)

        # obviously this form of
        # synchronization is dumb
        # and a more robust solution is required

        # start feeding the workers
        NO_OF_TASKS: int = 20
        print("Feeding workers ...")

        for i in range(NO_OF_TASKS):
            task = random.randint(0, 10_000)
            print(f"Feeding {i}: {task}")
            ventilation_socket.send_pyobj(task)

        print("Ventilation finalized")
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        ventilation_socket.close()
        context.term()

    print("Ventilator STOP")
