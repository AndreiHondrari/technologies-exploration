from typing import Optional
from functools import partial

import attr

hprint = partial(print, "\n#")


@attr.define(kw_only=True)
class Item:
    a: Optional[str] = attr.field(
        converter=attr.converters.optional(str)
    )


if __name__ == '__main__':
    item = Item(a=123)
    print(item)

    item = Item(a=None)
    print(item)
