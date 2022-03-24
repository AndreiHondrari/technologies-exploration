from functools import partial

import attr

hprint = partial(print, "\n#")


@attr.define(kw_only=True)
class Item:
    x: int
    y: int


def main() -> None:
    item = Item(x=11, y=22)

    hprint("As dict")
    item_dict = attr.asdict(item)
    print(item, "->", item_dict)

    hprint("As tuple")
    item_tuple = attr.astuple(item)
    print(item, "->", item_tuple)


if __name__ == "__main__":
    main()
