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
            print('-' * 20)
            print("Polling ...")
            polled = dict(poller.poll())

            msg = []
            while True:
                try:
                    # we just take whatever there is
                    # in the buffer, iregardless
                    # of the fact that it represents
                    # a last frame or not, for a given
                    # multipart message
                    msg_part = sock.recv_string(zmq.DONTWAIT)
                    msg.append(msg_part)
                except zmq.Again:
                    print("No more parts")
                    break

            when = time.strftime("%H:%M:%S")
            print(f"[{when}] Received", msg, flush=True)

    except KeyboardInterrupt:
        print("\nReceiver terminated")
