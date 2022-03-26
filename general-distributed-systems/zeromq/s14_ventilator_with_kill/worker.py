import random
import time

import zmq


def main() -> None:
    UID = random.randint(1000, 10_000)
    print(f"Starting worker [{UID}]")
    ctx = zmq.Context()

    ventilator = ctx.socket(zmq.PULL)
    ventilator.connect("tcp://localhost:5555")

    sink = ctx.socket(zmq.PUSH)
    sink.connect("tcp://localhost:6666")

    # the kill socket that will listen
    kill_sock = ctx.socket(zmq.SUB)
    kill_sock.connect("tcp://localhost:8888")
    kill_sock.setsockopt(zmq.SUBSCRIBE, b'')

    poller = zmq.Poller()
    poller.register(ventilator)
    poller.register(kill_sock)

    print(f"[{UID}] start processing")
    try:
        while True:
            polled = dict(poller.poll())

            if ventilator in polled:
                val = ventilator.recv_pyobj()
                print(f"[{UID}] PRCS", val)
                sink.send_pyobj((UID, val,))
                time.sleep(random.random() / 10)

            if kill_sock in polled:
                print(f"[{UID}] KILL")
                break

    except KeyboardInterrupt:
        print(f"\nWorker [{UID}] terminated")
    finally:
        print("Cleaning ...")
        ventilator.close()
        sink.close()
        kill_sock.close()
        ctx.term()

    print(f"[{UID}] finished")


if __name__ == '__main__':
    main()
