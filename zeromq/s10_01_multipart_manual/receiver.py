import time
import zmq


if __name__ == '__main__':
    print("Starting receiver ...")

    print("Advertise socket ...")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:5555")

    print("Register polling")
    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    print("Start receiving ....")
    try:
        while True:
            polled = dict(poller.poll())

            when = time.strftime("%H:%M:%S")
            print(f"[{when}] Messages detected", flush=True)

            # process all multipart messages on the wire
            while True:
                msg = []
                message_presence = True
                more = True

                # gather all the frames for a given multipart message
                # until there are no more frames for the current multipart
                # message
                while more:
                    try:
                        frame = sock.recv(zmq.DONTWAIT, copy=False)
                        more = frame.more
                        msg.append(frame.bytes.decode())

                    # check if the buffer has emptied
                    except zmq.Again:
                        print("No more messages")
                        message_presence = False
                        break

                # break out of the messages processing loop
                # to reach the poller again
                if not message_presence:
                    break

                print("Received", msg, flush=True)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()

    print("Receiver STOP")
