import zmq
from zmq.utils.monitor import parse_monitor_message

from events import EVENTS_MAP


def main() -> None:
    print("Start replier")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)

    monitor = sock.get_monitor_socket()

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)
    poller.register(monitor, zmq.POLLIN)

    sock.bind("ipc://gandalf")

    try:
        # event loop
        while True:
            # wait for either message or event
            polled = dict(poller.poll())

            # handle events
            if monitor in polled:
                try:
                    while True:
                        event_raw = monitor.recv_multipart(zmq.DONTWAIT)
                        print("EVENT_RAW", event_raw, flush=True)

                        event = parse_monitor_message(event_raw)
                        event_name = EVENTS_MAP[event['event']]
                        print("EVENT", event_name, event, flush=True)
                except zmq.ZMQError:
                    print("NO EVENTS", flush=True)

            # handle message
            if sock in polled:
                msg = sock.recv_string()
                print("SOCK_RECV", msg, flush=True)
                print("REPL")
                sock.send_string(f"GOT {msg}")

            print("----\n")

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
