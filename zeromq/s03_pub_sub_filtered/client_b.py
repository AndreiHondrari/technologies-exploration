import random

import zmq

CATEGORY = "category_2"


if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting client [{UID}]...")
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")

    socket.setsockopt_string(zmq.SUBSCRIBE, CATEGORY)

    print("Listening for news")
    while True:
        message = socket.recv_string()
        print(f"[{UID}] news: {message}")
