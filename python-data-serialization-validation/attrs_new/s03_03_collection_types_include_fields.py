from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    x: int
    y: int
    z: int

    t1: str = attr.field(default="N/A")
    t2: str = attr.field(default="N/A")


def main() -> None:
    item = Item(x=11, y=22, z=33)

    item_dict = attr.asdict(
        item,
        filter=attr.filters.include(
            attr.fields(Item).z,  # z attribute specifically
            str  # string types
        )
    )
    print(item, "->", item_dict)


if __name__ == "__main__":
    main()
