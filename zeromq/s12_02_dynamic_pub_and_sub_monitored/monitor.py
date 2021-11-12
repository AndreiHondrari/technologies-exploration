import time

import zmq


def main() -> None:
    print("Monitor started")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:8888")

    while True:
        intercepted = sock.recv_string()
        when = time.strftime("%M:%S")
        print(when, intercepted)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitor terminated")
