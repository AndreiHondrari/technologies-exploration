import time

import zmq


def main() -> None:
    print("SERVER START")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.REP)
    sock.bind("tcp://127.0.0.1:5555")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    msg_count = 0
    try:
        while True:
            polled = dict(poller.poll())

            if sock in polled:
                try:
                    while True:
                        sock.recv()
                        # sock.recv(zmq.DONTWAIT)
                        sock.send(b'-' * 100)
                        msg_count += 1
                        if msg_count % 100 == 0:
                            when = time.strftime("%H:%M:%S")
                            print(f"[{when}] {msg_count}")
                except zmq.Again:
                    when = time.strftime("%H:%M:%S")
                    print(f"[{when}] ON_AGAIN {msg_count}")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        sock.close(0)
        ctx.term()

    print(f"FINAL COUNT {msg_count}")

    print("SERVER STOP")


if __name__ == "__main__":
    main()
