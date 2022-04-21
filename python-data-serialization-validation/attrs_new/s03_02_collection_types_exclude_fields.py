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

    hprint("Excluding fields with lambda")
    item_dict = attr.asdict(
        item,
        filter=lambda field, value: field.name != "z"
    )
    print(item, "->", item_dict)

    hprint("Excluding fields with lambda (with fields)")
    item_dict = attr.asdict(
        item,
        filter=lambda field, value: field != attr.fields(Item).z
    )
    print(item, "->", item_dict)

    hprint("Excluding fields with premade filter")
    item_dict = attr.asdict(
        item,
        filter=attr.filters.exclude(
            attr.fields(Item).z,  # z attribute specifically
            str  # string types
        )
    )
    print(item, "->", item_dict)


if __name__ == "__main__":
    main()
