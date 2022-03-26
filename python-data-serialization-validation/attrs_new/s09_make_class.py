from functools import partial

import attr

hprint = partial(print, "\n#")


if __name__ == '__main__':
    Item = attr.make_class(
        "Item", {
            'x': attr.field(default=0),
            'y': attr.field(default=0),
        },
        kw_only=True
    )

    item = Item(x=11, y=22)
    print(item)
