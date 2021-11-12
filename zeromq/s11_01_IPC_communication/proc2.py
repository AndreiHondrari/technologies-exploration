import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PULL)
    sock.bind("ipc://gandalf")

    try:
        while True:
            msg = sock.recv_string()
            print("Received", msg, flush=True)
    except KeyboardInterrupt:
        print("\nProc 2 interrupted")
