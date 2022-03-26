import zmq

if __name__ == '__main__':
    print("Receiver START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)

    print("Connecting ...")
    sock.connect("tcp://localhost:5555")

    print("Start receiving ...")
    try:
        sock.recv()
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        sock.close()
        ctx.term()

    print("Receiver STOP")
