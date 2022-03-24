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


@attr.define(kw_only=True)
class Item:
    a: int = attr.field(validator=is_positive)


if __name__ == '__main__':
    hprint("Bad init")
    try:
        item = Item(a=-123)  # NOTICE THE MINUS SIGN
        print(item)
    except ValueError as e:
        print("EXC: ", repr(e))

    hprint("Good init")
    item = Item(a=123)
