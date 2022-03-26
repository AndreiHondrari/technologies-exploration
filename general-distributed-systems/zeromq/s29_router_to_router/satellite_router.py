
import time

from random import random, randint
from typing import Any, Dict, Optional

import zmq
from zmq.utils.monitor import recv_monitor_message


def tprint(*args: Any, **kwargs: Any) -> None:
    kwargs.update({'flush': True}, **kwargs)
    when = time.strftime("%H:%M:%S")
    print(when, *args, **kwargs)


CENTRAL_ROUTING_ID = b'\x00\x00\x00\xff'


def fetch_event(
    monitor: zmq.Socket,
    poller: zmq.Poller
) -> Optional[Dict[str, Any]]:

    polled = dict(poller.poll(0))

    if monitor in polled:
        return recv_monitor_message(monitor)

    return None


def wait_until_fully_connect(
    monitor: zmq.Socket,
    poller: zmq.Poller,
) -> None:
    is_connect_detected = False
    is_handshake_successful_detected = False

    while not is_connect_detected or not is_handshake_successful_detected:
        event: Optional[Dict[str, Any]] = fetch_event(monitor, poller)

        if event is not None:
            e_code = event['event']

            if e_code == zmq.EVENT_CONNECTED:
                tprint("EVENT: CONNECT")
                is_connect_detected = True

            if e_code == zmq.EVENT_HANDSHAKE_SUCCEEDED:
                tprint("EVENT: HANDSHAKE SUCCESS")
                is_handshake_successful_detected = True


def check_if_disconnected(
    monitor: zmq.Socket,
    poller: zmq.Poller,
) -> bool:
    while True:
        event: Optional[Dict[str, Any]] = fetch_event(monitor, poller)
        if event is None:
            break

        e_code = event['event']
        if e_code == zmq.EVENT_DISCONNECTED:
            return True

    return False


def main() -> None:
    UID = randint(1000, 10_000)
    tprint(f"SATELLITE [{UID}] START")

    ctx = zmq.Context()
    central_router = ctx.socket(zmq.ROUTER)

    monitor = central_router.get_monitor_socket()

    poller = zmq.Poller()
    poller.register(monitor, zmq.POLLIN)

    central_router.setsockopt(zmq.ROUTER_MANDATORY, True)

    try:
        central_router.connect("tcp://127.0.0.1:7777")

        tprint("Wait for initial connection ...")
        wait_until_fully_connect(monitor, poller)

        for i in range(5):
            # monitor connection events
            if check_if_disconnected(monitor, poller):
                tprint(
                    "Central router disconnected. "
                    "Waiting for reconnect ..."
                )
                wait_until_fully_connect(monitor, poller)

            # send something
            value = randint(100, 1000)
            tprint("SND", value)

            central_router.send_multipart(
                [
                    CENTRAL_ROUTING_ID,
                    value.to_bytes(4, 'big')
                ],
            )

            time.sleep(0.3 + 0.7 * random())

    except KeyboardInterrupt:
        tprint("\nCtrl+C detected")

    except zmq.ZMQError as zerr:
        tprint(
            "Exception caught in main:",
            zerr.errno,
            zerr.msg,
        )

    finally:
        tprint("Disable monitor ...")
        central_router.disable_monitor()
        monitor.close(1)

        tprint("Closing socket ...")
        central_router.close(1)

    tprint("Closing context ...")
    ctx.term()

    tprint(f"SATELLITE [{UID}] STOP")


if __name__ == "__main__":
    main()
