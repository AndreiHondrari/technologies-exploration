import zmq


def main() -> None:
    print("Start subscriber")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, "kogaion")
    sock.setsockopt_string(zmq.SUBSCRIBE, "excalibur")
    sock.setsockopt_string(zmq.SUBSCRIBE, "baldur")
    sock.connect("ipc://gandalf")

    try:
        while True:
            msg = sock.recv_string()
            print("RECV", msg, flush=True)

    except KeyboardInterrupt:
        print("\nStop detected!")
    finally:
        print("Cleaning ...")
        sock.close()
        ctx.term()
    print("DONE")


if __name__ == '__main__':
    main()
