import attr


@attr.s
class SomeClass:
    a: int = attr.ib()
    b: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(11, 900)
    o2 = SomeClass(22, 10)
    print(o1 < o2)
