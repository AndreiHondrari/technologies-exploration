import zmq

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REP)
    sock.bind("ipc://gandalf")

    try:
        while True:
            msg = sock.recv_pyobj()
            print("Received", msg, flush=True)
            sock.send_pyobj(msg)
            print("Reply", flush=True)
    except KeyboardInterrupt:
        print("\nProc 2 interrupted")
