from pprint import pprint as pp
from functools import partial

import msgpack

hprint = partial(print, " \n#")


def main() -> None:
    hprint("Original data")
    d1 = 123456
    d2 = [0xff, 0xbb, 0xcc, 0x99]
    d3 = {'a': "Kerosene", 'b': "Gandalf"}

    pp(d1)
    pp(d2)
    pp(d3)

    hprint("Serialize")
    e1 = msgpack.packb(d1)
    e2 = msgpack.packb(d2)
    e3 = msgpack.packb(d3)

    pp(e1)
    pp(e2)
    pp(e3)

    hprint("Decode")
    x1 = msgpack.unpackb(e1)
    x2 = msgpack.unpackb(e2)
    x3 = msgpack.unpackb(e3)

    pp(x1)
    pp(x2)
    pp(x3)


if __name__ == "__main__":
    main()
