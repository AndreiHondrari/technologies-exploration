import attr


@attr.s
class SomeClass:
    x: int = attr.ib(kw_only=True)
    y: int = attr.ib(kw_only=True)


@attr.s(kw_only=True)
class SomeClassB:
    a: int = attr.ib()
    b: int = attr.ib()


if __name__ == '__main__':

    # SomeClass
    try:
        o1 = SomeClass(11, 22)  # type: ignore
        print("o1", o1)
    except Exception as e:
        print("Caught exception: ", e)

    o2 = SomeClass(x=11, y=22)
    print(o2)

    # SomeClassB
    try:
        o3 = SomeClassB(11, 22)  # type: ignore
        print("o3", o3)
    except Exception as e:
        print("Caught exception: ", e)

    o4 = SomeClassB(a=11, b=22)
    print(o4)
