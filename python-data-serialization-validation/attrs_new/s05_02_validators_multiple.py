from typing import Any
from functools import partial

import attr

hprint = partial(print, "\n#")


def is_positive(
    inst: Any,
    prop: attr.Attribute,
    val: int
) -> None:
    if val < 0:
        raise ValueError(f"Value must be positive. {val} is not")


def is_not_333(
    inst: Any,
    prop: attr.Attribute,
    val: int
) -> None:
    if val == 333:
        raise ValueError("Must not be 333")


@attr.define(kw_only=True)
class Item:
    a: int = attr.field(
        validator=[is_positive, is_not_333]
    )


if __name__ == '__main__':
    hprint("Bad init (negative number)")
    try:
        item = Item(a=-123)  # NOTICE THE MINUS SIGN
        print(item)
    except ValueError as e:
        print("EXC: ", repr(e))

    hprint("Bad init (333)")
    try:
        item = Item(a=333)
        print(item)
    except ValueError as e:
        print("EXC: ", repr(e))

    hprint("Good init")
    item = Item(a=999)
