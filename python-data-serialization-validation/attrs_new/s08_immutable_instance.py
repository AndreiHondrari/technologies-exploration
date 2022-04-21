from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.frozen(kw_only=True)
class Item:
    x: int
    y: int


if __name__ == '__main__':
    hprint("Simple init")
    i1 = Item(x=11, y=22)
    print(i1)

    hprint("Try to change an attribute")
    try:
        i1.x = 33  # type: ignore[misc]  # it tells us that it is readonly
        print(i1)
    except attr.exceptions.FrozenInstanceError as fierr:
        print("EXC: ", repr(fierr))

    hprint("Evolve")
    i2 = attr.evolve(i1, x=33)
    print(i2)
