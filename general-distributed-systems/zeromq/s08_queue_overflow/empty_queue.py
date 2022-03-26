import time
import zmq


if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)

    sock.bind("tcp://127.0.0.1:5559")

    SLEEP_TIME = 7
    print(f"SLEEP ({SLEEP_TIME}s)")
    time.sleep(SLEEP_TIME)
    print("AWAKE")

    while True:
        try:
            sock.recv(flags=zmq.NOBLOCK)
            print(".", end="", flush=True)
        except zmq.Again as e:
            print(repr(e))
            break

    print("DONE")
