from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(order=True)
class Item:
    a: int
    b: int


if __name__ == '__main__':
    o1 = Item(11, 900)
    o2 = Item(22, 10)
    o3 = Item(11, 900)

    hprint("o1 == o2")
    print(o1 == o2)

    hprint("o1 == o3")
    print(o1 == o3)

    hprint("o1 < o2")
    print(o1 < o2)
