import attr


@attr.s(kw_only=True)
class SomeClass:
    a = attr.ib(type=str)


@attr.s(kw_only=True, auto_attribs=True)
class SomeClassB:
    b: str


if __name__ == '__main__':
    o1 = SomeClass(a="foo")
    print("o1", o1)

    o2 = SomeClassB(b="foo")
    print("o2", o2)
