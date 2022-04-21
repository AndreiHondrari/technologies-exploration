from functools import partial

import attr

hprint = partial(print, " \n#")


def convert_to_something(value: int) -> int:
    # NOTICE that we change the value not the type of the value
    return value * 2


@attr.define(kw_only=True)
class Item:
    a: int = attr.field(converter=convert_to_something)


if __name__ == '__main__':
    item = Item(a=111)
    print(item)
