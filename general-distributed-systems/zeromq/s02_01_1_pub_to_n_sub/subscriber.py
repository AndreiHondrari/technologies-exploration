import random

import zmq


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting subscriber [{UID}]...")
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")

    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Listening for news")
    try:
        while True:
            message = socket.recv_string()
            print(f"[{UID}] news: {message}", flush=True)
    except KeyboardInterrupt:
        print(f"\nSubscriber [{UID}] terminated")
