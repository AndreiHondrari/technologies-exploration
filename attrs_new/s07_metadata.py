"""
This feature is per-class only and it is for thirdparty
development mostly
"""

import enum
from functools import partial

import attr

hprint = partial(print, "\n#")


@enum.unique
class Foo(enum.IntEnum):
    BAR = enum.auto()
    BAZ = enum.auto()


@attr.define(kw_only=True)
class Item:
    a: int = attr.field(metadata={'foo': Foo.BAR})


if __name__ == '__main__':
    print(attr.fields(Item).a.metadata)
