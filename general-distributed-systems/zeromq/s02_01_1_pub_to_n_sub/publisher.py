import time
import random
import string

import zmq


if __name__ == '__main__':
    print("Starting publisher ...")
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    print("Sending")
    try:
        while True:
            message = "".join(random.sample(string.ascii_letters, 10))
            print(f"Sending {message}", flush=True)
            socket.send_string(message)
            time.sleep(random.random())
    except KeyboardInterrupt:
        print("\nPublisher terminated")
