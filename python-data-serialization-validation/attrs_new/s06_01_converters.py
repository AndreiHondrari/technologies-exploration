from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    a: str = attr.field(converter=str)


if __name__ == '__main__':
    item = Item(a=123)
    print(item)
