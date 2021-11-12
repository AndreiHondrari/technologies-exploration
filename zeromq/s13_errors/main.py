import zmq


if __name__ == '__main__':
    for i in range(1, 107):
        print(i, zmq.strerror(i))
