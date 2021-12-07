import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    sock.connect("tcp://localhost:5555")

    print("Binary send")
    val = 12345
    data = val.to_bytes(750_000_000, 'big')
    tracker = sock.send(data, copy=False, track=True)
    print("ISDONE", tracker.done)
    print("SENT")
    tracker.wait()
    print("ISDONE", tracker.done)
    print("DONE")
