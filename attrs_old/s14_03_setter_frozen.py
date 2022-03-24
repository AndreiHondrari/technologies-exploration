import attr


@attr.s
class SomeClass:
    a: int = attr.ib(on_setattr=attr.setters.frozen)
    b: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(11, 22)

    # try to change frozen field
    try:
        o1.a = 33
    except attr.exceptions.FrozenAttributeError as e:
        print("Caught exception:", repr(e))

    # change non-frozen field
    o1.b = 55
