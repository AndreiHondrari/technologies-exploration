from typing import Any
from functools import partial

import attr

hprint = partial(print, " \n#")


def set_callback(
    instance: "Item",
    attribute: attr.Attribute,  # type: ignore[type-arg]
    value: Any
) -> None:
    print(f"SET {value} for {attribute.name}")


@attr.define(on_setattr=set_callback)
class Item:
    a: int
    b: int


if __name__ == '__main__':
    item = Item(11, 900)
    item.a = 99
    item.b = 777
