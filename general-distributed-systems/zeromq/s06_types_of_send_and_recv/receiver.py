import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)

    sock.bind("tcp://*:5555")

    print("Binary recv")
    data = sock.recv()
    val = int.from_bytes(data, 'big')
    print(f"{data} -> {val}")

    print("\nString send")
    val = sock.recv_string()
    print(val)

    print("\nJSON send")
    val = sock.recv_json()
    print(val)

    print("\nPyObj send")
    val = sock.recv_pyobj()
    print(val)
