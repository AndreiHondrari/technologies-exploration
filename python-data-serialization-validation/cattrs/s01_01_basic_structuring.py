from functools import partial

import attr
import cattr

hprint = partial(print, " \n#")


@attr.define
class Item:
    x: int
    c: float
    t: str


def main() -> None:
    hprint("Structure with malformed input")
    d1 = {'a': 11}
    try:
        result = cattr.structure(d1, Item)
    except KeyError as kerr:
        print("Caught exception: ", repr(kerr))

    hprint("Structure with complete input")
    d2 = {'x': 22, 'c': 55.78, 't': "something"}
    result = cattr.structure(d2, Item)
    print(result)


if __name__ == "__main__":
    main()
