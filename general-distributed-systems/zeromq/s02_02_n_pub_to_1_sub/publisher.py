import time
import random
import string

import zmq


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting publisher [{UID}] (as connecter)...")
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect("tcp://localhost:5556")

    print("Sending")
    try:
        while True:
            message = "".join(random.sample(string.ascii_letters, 10))
            message = f"[{UID}] " + message
            print(f"Sending {message}", flush=True)
            socket.send_string(message)
            time.sleep(random.random())
    except KeyboardInterrupt:
        print(f"\nPublisher [{UID}] terminated")
