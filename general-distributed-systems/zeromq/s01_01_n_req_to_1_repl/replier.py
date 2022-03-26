import time
import random

import zmq


if __name__ == '__main__':
    print("Starting replier (as advertiser) ...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Replier listening")
    try:
        while True:
            message = socket.recv()
            print(f"Received request: {message}", flush=True)
            time.sleep(0.1)
            reply = f"Reply {random.randint(0, 100)}"
            print("Replying", reply, flush=True)
            socket.send_string(reply)
    except KeyboardInterrupt:
        print("\nReplier terminated")
