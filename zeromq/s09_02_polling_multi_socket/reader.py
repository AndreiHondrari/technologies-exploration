import zmq

if __name__ == '__main__':
    print("Starting reader ...")
    ctx = zmq.Context()

    print("Acquiring sockets")
    sender1_sock = ctx.socket(zmq.PULL)
    sender1_sock.connect("tcp://localhost:5551")

    sender2_sock = ctx.socket(zmq.PULL)
    sender2_sock.connect("tcp://localhost:5552")

    print("Registering sockets for polling")
    poller = zmq.Poller()
    poller.register(sender1_sock, zmq.POLLIN)
    poller.register(sender2_sock, zmq.POLLIN)

    print("Start reading")
    try:
        while True:
            polled = dict(poller.poll())

            if sender1_sock in polled:
                msg1 = sender1_sock.recv_string()
                print("S1", msg1)

            if sender2_sock in polled:
                msg2 = sender2_sock.recv_string()
                print("S2", msg2)

    except KeyboardInterrupt:
        print("\nREADER DONE")
