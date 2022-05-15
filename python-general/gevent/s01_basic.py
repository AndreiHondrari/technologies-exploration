import time
import random as rd
from typing import List

import gevent
from gevent import Greenlet


def somefunc(name: str) -> None:
    print(f"{name} START")

    for i in range(3):
        print(name, i)
        gevent.sleep(0)  # release execution for next greenlet
        time.sleep(rd.random())

    print(f"{name} STOP")


def main() -> None:
    print("START")

    greenlets: List[Greenlet] = []

    for i in range(3):
        new_greenlet = Greenlet(somefunc, f"{i:0>4}")
        new_greenlet.start()
        greenlets.append(new_greenlet)

    gevent.wait()

    print("DONE")


if __name__ == "__main__":
    main()
