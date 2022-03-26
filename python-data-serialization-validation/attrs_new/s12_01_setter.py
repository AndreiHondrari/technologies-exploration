from functools import partial

import attr

hprint = partial(print, "\n#")


def set_a_callback(
    instance: "Item",
    attribute: attr.Attribute,  # type: ignore[type-arg]
    value: int
) -> None:
    print(f"SET {value} for {attribute.name}")


@attr.define
class Item:
    a: int = attr.field(on_setattr=set_a_callback)
    b: int


if __name__ == '__main__':
    item = Item(11, 900)
    item.a = 99
