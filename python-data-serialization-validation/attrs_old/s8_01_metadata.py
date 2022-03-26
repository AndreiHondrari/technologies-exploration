import enum

import attr


@enum.unique
class Foo(enum.IntEnum):
    BAR = enum.auto()
    BAZ = enum.auto()


@attr.s(kw_only=True)
class SomeClass:
    a: int = attr.ib(metadata={'foo': Foo.BAR})


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1)
    print("meta o1", attr.fields(SomeClass).a.metadata)
