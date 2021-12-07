import datetime

import zmq


def main() -> None:
    print("START REQUESTER")

    try:
        while True:
            moment = datetime.datetime.today().isoformat()
            print(f"CYCLE {moment}", flush=True)

            ctx = zmq.Context()
            replier = ctx.socket(zmq.REQ)
            replier.connect("tcp://localhost:4567")
            replier.send_string("")
            replier.close()
            ctx.term()

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    print("STOP")


if __name__ == '__main__':
    main()
