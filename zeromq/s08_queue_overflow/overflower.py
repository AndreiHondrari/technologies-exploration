import time
import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    sock.connect("tcp://localhost:5559")

    SLEEP_TIME = 1
    print(f"SLEEP ({SLEEP_TIME}s)")
    time.sleep(SLEEP_TIME)
    print("AWAKE")

    print("Start sending")
    count = 0
    while True:
        try:
            sock.send(b'abc', flags=zmq.NOBLOCK)
        except zmq.ZMQError as e:
            print(repr(e))
            break

        count += 1
        if count % 100 == 0:
            print(f"{count}", flush=True)

    print("DONE")
