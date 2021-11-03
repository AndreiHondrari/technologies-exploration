import attr


@attr.s
class SomeClass:
    x: int = attr.ib()
    y: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(11, 22)
    print("o1", o1)

    o2 = SomeClass(y=22, x=11)
    print("o2", o2)
