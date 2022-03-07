import zmq

if __name__ == '__main__':
    print("Sender START")
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUSH)

    print("Binding ...")
    sock.bind("tcp://*:5555")

    # notice there is no send, just close

    print("Closing ...")
    sock.close()
    ctx.term()
    print("Sender STOP")
