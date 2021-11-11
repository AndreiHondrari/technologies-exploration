import random
import time

import zmq

if __name__ == '__main__':
    UID = random.randint(1000, 10_000)
    print(f"Starting sender TWO [{UID}] ...")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)
    sock.bind("tcp://127.0.0.1:5552")

    print(f"[{UID}] Start sending")
    try:
        while True:
            val = random.randint(0, 1000)
            msg = f"[{UID}] {val}"
            print(f"[{UID}] Sending '{msg}'", flush=True)
            sock.send_string(msg)
            time.sleep(1.5)
    except KeyboardInterrupt:
        print(f"\nSender [{UID}] terminated")
