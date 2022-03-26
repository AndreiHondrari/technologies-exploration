import attr


@attr.s(kw_only=True, frozen=True)
class SomeClass:
    a: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1, id(o1))

    o2 = attr.evolve(o1, a=321)

    print("o2", o2, id(o2))
