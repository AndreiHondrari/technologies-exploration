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
            print(f"[{when}] Multipart detected", flush=True)
            msg = []
            while True:
                try:
                    msg.append(sock.recv_string(zmq.DONTWAIT))
                except zmq.Again:
                    print("Multipart read finished")
                    break

            print("Received", msg, flush=True)

    except KeyboardInterrupt:
        print("\nReceiver terminated")
