from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class SubItem:
    t1: str = attr.field(default="N/A")
    t2: str = attr.field(default="N/A")


@attr.define(kw_only=True)
class Item:
    x: int
    y: int
    z: int
    subitem: SubItem


def main() -> None:
    subitem = SubItem(t1="something", t2="something else")
    item = Item(x=11, y=22, z=33, subitem=subitem)

    item_dict = attr.asdict(item)
    print(item, "->", item_dict)


if __name__ == "__main__":
    main()
