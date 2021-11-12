import time
import random

import zmq


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting replier [{UID}] (as client)...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://localhost:5555")

    print("Replier listening")
    try:
        while True:
            message = socket.recv()
            print(f"Received request: {message}")
    except KeyboardInterrupt:
        print(f"\nReplier [{UID}] terminated")
