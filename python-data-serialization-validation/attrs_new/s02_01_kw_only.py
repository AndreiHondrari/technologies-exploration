from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class ItemA:
    x: int
    k: float
    t: str


@attr.define
class ItemB:
    x: int = attr.field(kw_only=True)
    k: float = attr.field(kw_only=True)
    t: str = attr.field(kw_only=True)


def main() -> None:
    hprint("Attempt at initialization without keywords")
    try:
        item_a = ItemA(10, 26.89, "blabla")  # type: ignore
        print(item_a)
    except Exception as exc:
        print("EXC: ", repr(exc))

    hprint("Correct initialization")
    item_a = ItemA(x=10, k=26.89, t="blabla")
    print(item_a)

    hprint("Initialization when kw_only on fields")
    item_b = ItemB(x=10, k=26.89, t="blabla")
    print(item_b)


if __name__ == "__main__":
    main()
