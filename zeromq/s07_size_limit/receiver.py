import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)

    sock.bind("tcp://*:5555")

    while True:
        print("Binary recv")
        data = sock.recv()
        val = int.from_bytes(data, 'big')
        print(f"{len(data)} -> {val}")
