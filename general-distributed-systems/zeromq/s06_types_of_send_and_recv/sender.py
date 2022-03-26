import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    sock.connect("tcp://localhost:5555")

    print("Binary send")
    val = 12345
    data = val.to_bytes(val.bit_length() // 8 + 1, 'big')
    sock.send(data)
    print(f"{val} -> {data}")

    print("\nString send")
    val = "some string"
    print(val)
    sock.send_string(val)

    print("\nJSON send")
    val = {'x': 55, 'y': 77}
    print(val)
    sock.send_json(val)

    print("\nPyObj send")
    val = [11, 22, 33, 44]
    print(val)
    sock.send_pyobj(val)
