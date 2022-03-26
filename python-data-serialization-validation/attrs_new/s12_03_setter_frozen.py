from typing import Any
from functools import partial

import attr

hprint = partial(print, "\n#")


def set_callback(
    instance: "Item",
    attribute: attr.Attribute,  # type: ignore[type-arg]
    value: Any
) -> None:
    print(f"SET {value} for {attribute.name}")


@attr.define
class Item:
    a: int
    b: int = attr.field(on_setattr=attr.setters.frozen)


if __name__ == '__main__':
    item = Item(11, 900)

    hprint("Set a")
    item.a = 99
    print(item)

    hprint("Set b")
    try:
        item.b = 777
    except attr.exceptions.FrozenAttributeError as faerr:
        print("EXC:", repr(faerr))

    print(item)
