import random

import zmq

CATEGORY = "category_2"


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting client [{UID}]...")
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, CATEGORY)
    socket.connect("tcp://localhost:5556")

    print("Listening for news")
    try:
        while True:
            message = socket.recv_string()
            print(f"[{UID}] news: {message}")
    except KeyboardInterrupt:
        print("\nClient B terminated")
