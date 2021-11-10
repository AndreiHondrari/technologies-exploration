import time

import zmq


if __name__ == '__main__':
    print("Starting server ...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Server listening")
    while True:
        message = socket.recv()
        print(f"Received request: {message}")
        time.sleep(0.1)
        socket.send_string("World")
