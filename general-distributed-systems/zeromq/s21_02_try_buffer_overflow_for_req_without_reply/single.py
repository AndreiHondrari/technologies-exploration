import zmq


def main() -> None:
    print("[SINGLE_CLIENT] START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:5555")

    try:
        print("PING", flush=True)
        sock.send(b'PING' * 50)

        sock.recv()
        print("PONG")

    except KeyboardInterrupt:
        print("\n[SINGLE_CLIENT] SIGINT detected")

    print("[SINGLE_CLIENT] Cleaning ...")
    sock.close(1)

    ctx.term()

    print("[SINGLE_CLIENT] STOP")


if __name__ == "__main__":
    main()
