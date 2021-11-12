import time

import zmq


def main() -> None:
    print("Proxy started")
    ctx = zmq.Context()

    xsub = ctx.socket(zmq.SUB)
    xsub.bind("tcp://127.0.0.1:5555")
    xsub.setsockopt(zmq.SUBSCRIBE, b'')

    xpub = ctx.socket(zmq.PUB)
    xpub.bind("tcp://127.0.0.1:7777")

    while True:

        frame = xsub.recv(copy=False)

        when = time.strftime("%M:%S")
        print(f"[{when}] INTRCPT {frame.bytes}")

        xpub.send(frame, copy=False)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProxy terminated")
