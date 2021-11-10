import random
import zmq


if __name__ == '__main__':
    UID: int = random.randint(1000, 10_000)
    print(f"Starting client [{UID}] ...")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Client sending")
    for i in range(10):
        socket.send_string(f"[{UID}] Hey {i}")
        reply = socket.recv()
        print(f"Received reply: {reply}")
