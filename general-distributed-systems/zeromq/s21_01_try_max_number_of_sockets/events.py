
import zmq

EVENTS_MAP = {}

EVENT_NAMES = [x for x in dir(zmq) if 'EVENT_' in x]

for ev_name in EVENT_NAMES:
    EVENTS_MAP[getattr(zmq, ev_name)] = ev_name
