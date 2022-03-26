import zmq


if __name__ == '__main__':
    print(f"Starting subscriber (as advertiser)...")
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind("tcp://127.0.0.1:5556")

    # subscribe to all messages
    # or otherwise said: no filter / empty filter
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Listening for news")
    try:
        while True:
            message = socket.recv_string()
            print(f"News: {message}", flush=True)
    except KeyboardInterrupt:
        print("\nSubscriber terminated")
