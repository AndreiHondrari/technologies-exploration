import zmq

if __name__ == '__main__':
    print("Sink START")
    context = zmq.Context()
    sink = context.socket(zmq.PULL)

    print("Advertising sink")
    sink.bind("tcp://*:5558")

    print("Collecting ...")
    try:
        i: int = 1
        while True:
            task_result = sink.recv_pyobj()
            print(f"Received {i}: {task_result}")
            i += 1
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        sink.close()
        context.term()

    print("Sink STOP")
