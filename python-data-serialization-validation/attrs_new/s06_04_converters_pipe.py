from functools import partial

import attr

hprint = partial(print, " \n#")


def double_value(value: int) -> int:
    return value * 2


def add_10(value: int) -> int:
    return value + 10


@attr.define(kw_only=True)
class Item:
    a: int = attr.field(
        converter=attr.converters.pipe(  # type: ignore[misc]
            double_value, add_10
        )
    )

    b: int = attr.field(
        converter=attr.converters.pipe(  # type: ignore[misc]
            add_10, double_value
        )
    )


if __name__ == '__main__':
    item = Item(a=5, b=5)
    print(item)
