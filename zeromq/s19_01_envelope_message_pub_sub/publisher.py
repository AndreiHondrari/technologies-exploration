import time
import random

import zmq


def main() -> None:
    print("Start publisher")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.bind("ipc://gandalf")

    try:
        while True:
            msg1 = str(random.randint(100, 1000))
            msg2 = str(random.randint(100, 1000))
            msg3 = str(random.randint(100, 1000))

            envelope1 = [b'kogaion', msg1.encode()]
            envelope2 = [b'excalibur', msg2.encode()]
            envelope3 = [b'baldur', msg3.encode()]

            print("SND1", envelope1, flush=True)
            sock.send_multipart(envelope1)

            print("SND2", envelope2, flush=True)
            sock.send_multipart(envelope2)

            print("SND3", envelope3, flush=True)
            sock.send_multipart(envelope3)

            time.sleep(random.random())

    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()
    print("DONE")


if __name__ == '__main__':
    main()
