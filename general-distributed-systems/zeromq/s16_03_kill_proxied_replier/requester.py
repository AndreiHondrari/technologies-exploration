import time

import zmq


def main() -> None:
    print("Start requester")
    ctx = zmq.Context()

    sock = ctx.socket(zmq.REQ)
    sock.connect("tcp://localhost:5555")

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)

    try:
        while True:
            sock.send_string("PING")
            print("POLL")
            poller.poll()
            print("POST-POLL")
            reply = sock.recv_string()
            print("REPL", reply)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nKill detected")
    finally:
        print("Terminated")

    sock.close(0)
    ctx.term()


if __name__ == '__main__':
    main()
