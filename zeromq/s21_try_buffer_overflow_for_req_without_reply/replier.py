import time
import datetime

import zmq


def main() -> None:
    print("START REPLIER")
    ctx = zmq.Context()

    replier = ctx.socket(zmq.REP)
    replier.bind("tcp://*:4567")

    i = 1

    try:
        while True:
            moment = datetime.datetime.today().isoformat()
            print(f"CYCLE {i} {moment}", flush=True)

            print("RECV", flush=True)
            replier.recv_string()
            time.sleep(0.01)
            print("SND", flush=True)
            replier.send_string("")

            i += 1
    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    replier.close(linger=0)
    ctx.term()
    print("STOP")


if __name__ == '__main__':
    main()
