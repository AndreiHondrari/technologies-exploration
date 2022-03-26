
import argparse
import time

from random import randint
from typing import Any, Optional, Callable, Dict, cast

import zmq
from zmq.utils.monitor import recv_monitor_message


EVENTS_MAP = {}

EVENT_NAMES = [x for x in dir(zmq) if 'EVENT_' in x]

for ev_name in EVENT_NAMES:
    EVENTS_MAP[getattr(zmq, ev_name)] = ev_name


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


def fetch_event(
    monitor: zmq.Socket,
    poller: zmq.Poller
) -> Optional[Dict[str, Any]]:

    polled = dict(poller.poll(0))

    if monitor in polled:
        return cast(
            Callable[[zmq.Socket], Dict[str, Any]],
            recv_monitor_message
        )(monitor)

    return None


def main(socket_type: int) -> None:
    UID = randint(1000, 10_000)
    tprint(f"CONNECTER [{UID}] START")

    ctx = zmq.Context()  # type: ignore
    binder = ctx.socket(socket_type)  # type: ignore

    monitor = binder.get_monitor_socket()

    poller = zmq.Poller()  # type: ignore
    poller.register(monitor)

    try:
        binder.connect("tcp://127.0.0.1:7777")

        while True:
            poller.poll()

            event = fetch_event(monitor, poller)

            if event is not None:
                e_code = event['event']
                print()
                tprint('-' * 20)
                tprint("EVENT_CODE    :", e_code, EVENTS_MAP[e_code])
                tprint("EVENT_VALUE   :", event['value'])
                tprint("EVENT_ENDPOINT:", event['endpoint'])

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    tprint("Closing socket ...")
    binder.disable_monitor()
    monitor.close(1)
    binder.close(1)

    tprint("Closing context ...")
    ctx.term()  # type: ignore

    tprint(f"CONNECTER [{UID}] STOP")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        dest='socket_type',
        type=str,
        choices=zmq.utils.constant_names.socket_type_names,
        default='REP',
    )

    args = parser.parse_args()

    socket_type: int = getattr(zmq, args.socket_type)

    main(socket_type)
