import time

import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    sock.connect("tcp://localhost:5555")

    print("Binary send")
    val = 12345
    data = val.to_bytes(100_000_000, 'big')
    sock.send(data)
    print("SENT")
    time.sleep(2)
    print("DONE")
