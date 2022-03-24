from functools import partial

import attr

hprint = partial(print, "\n#")


@attr.define(kw_only=True)
class Item:
    a: int = attr.field()
    b: int = attr.field()

    @b.default
    def _b_default(self) -> int:
        return 42


if __name__ == '__main__':
    item = Item(a=11)
    print(item)
