import zmq


if __name__ == '__main__':
    print("Starting requester (as client)...")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Requester sending")
    try:
        i = 0
        while True:
            i += 1
            msg = f"Hey {i}"
            print("Sending", msg, flush=True)
            socket.send_string(msg)
            reply = socket.recv()
            print(f"Received reply: {reply}", flush=True)

    except KeyboardInterrupt:
        print("\nRequester terminated")
