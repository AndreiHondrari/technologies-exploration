import time
import random

import zmq
from zmq.utils.monitor import parse_monitor_message

from events import EVENTS_MAP


def main() -> None:
    print("Start requester")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)

    monitor = sock.get_monitor_socket()

    sock.connect("ipc://gandalf")

    try:
        # event loop
        while True:

            # check for any events
            try:
                while True:
                    event_raw = monitor.recv_multipart(zmq.DONTWAIT)
                    print("EVENT_RAW", event_raw, flush=True)

                    event = parse_monitor_message(event_raw)
                    event_name = EVENTS_MAP[event['event']]
                    print("EVENT", event_name, event, flush=True)
            except zmq.ZMQError:
                print("NO EVENTS", flush=True)

            # just send message
            msg = str(random.randint(1, 64))
            print("SND", msg, flush=True)
            sock.send_string(msg)

            reply = sock.recv_string()
            print("REPL", reply, flush=True)

            print("----\n")

            # wait a bit before doing stuff again
            time.sleep(random.random())

    except KeyboardInterrupt:
        print("\nStop detected")
    finally:
        print("Cleaning ...")
        sock.disable_monitor()
        monitor.close(linger=0)
        sock.close(linger=0)
        print("Terminating context ...")
        ctx.term()

    print("DONE")


if __name__ == '__main__':
    main()
