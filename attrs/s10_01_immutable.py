import attr


@attr.s(kw_only=True, frozen=True)
class SomeClass:
    a: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1)

    try:
        o1.a = 321
    except attr.exceptions.FrozenInstanceError as e:
        print("Caught exception: ", repr(e))
