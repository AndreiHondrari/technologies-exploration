import zmq


def main() -> None:
    print("Start service")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.REP)
    sock.bind("tcp://*:5678")

    try:
        while True:
            msg = sock.recv_string()
            print("RECV", msg)
            sock.send_string("PONG")
    except KeyboardInterrupt:
        print("\nKill detected")
    finally:
        print("Terminated")

    sock.close(0)
    ctx.term()


if __name__ == '__main__':
    main()
