from functools import partial

import attr

hprint = partial(print, " \n#")


def convert_to_something(value: int) -> str:
    return f"{value}_" * 10


@attr.define(kw_only=True)
class Item:
    a: str = attr.field(converter=convert_to_something)


if __name__ == '__main__':
    item = Item(a=123)
    print(item)
