import time
import random
import string

import zmq

CAT_1 = "category_1"
CAT_2 = "category_2"

if __name__ == '__main__':
    print("Starting server ...")
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5556")

    print("Sending")
    try:
        while True:
            message1 = "".join(random.sample(string.ascii_letters, 10))
            cat1message = f"{CAT_1} {message1}"

            message2 = "".join(random.sample(string.ascii_letters, 10))
            cat2message = f"{CAT_2} {message2}"

            print(f"Sending {cat1message}")
            socket.send_string(cat1message)

            print(f"Sending {cat2message}")
            socket.send_string(cat2message)

            time.sleep(random.random())
    except KeyboardInterrupt:
        print("\nServer interrupted")
