import zmq


if __name__ == '__main__':
    print("Starting requester (as advertiser) ...")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.bind("tcp://127.0.0.1:5555")

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
        print("\nRequster terminated")
