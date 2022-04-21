from typing import Optional
from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    a: Optional[str] = attr.field(
        converter=attr.converters.default_if_none("N/A")  # type: ignore[misc]
    )


if __name__ == '__main__':
    item = Item(a="something")
    print(item)

    item = Item(a=None)
    print(item)
