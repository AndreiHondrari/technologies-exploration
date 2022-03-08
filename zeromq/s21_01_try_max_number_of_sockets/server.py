import zmq

from zmq.utils.monitor import parse_monitor_message

from events import EVENTS_MAP


def main() -> None:
    print("SERVER START")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.PULL)
    monitor = sock.get_monitor_socket()
    sock.bind("tcp://127.0.0.1:5555")

    poller = zmq.Poller()
    poller.register(monitor, zmq.POLLIN)

    try:
        while True:
            polled = dict(poller.poll())
            if monitor in polled:
                print('-' * 20)
                try:
                    while True:
                        event_raw = monitor.recv_multipart(zmq.DONTWAIT)
                        event = parse_monitor_message(event_raw)
                        event_name = EVENTS_MAP[event['event']]
                        print("EVENT", event_name, event, flush=True)

                except zmq.Again:
                    print("No more events")

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        sock.disable_monitor()
        monitor.close(0)
        sock.close(0)

    print("SERVER STOP")




if __name__ == "__main__":
    main()
