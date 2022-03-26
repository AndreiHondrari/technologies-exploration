import attr


def validate_a(instance, attribute, value) -> None:
    print("VALIDATING:", attribute.name, value)


@attr.s
class SomeClass:
    a: int = attr.ib(validator=validate_a)
    b: int = attr.ib()


@attr.s
class SomeClassB:
    a: int = attr.ib(
        validator=validate_a,
        on_setattr=attr.setters.validate
    )


if __name__ == '__main__':
    # validated only at instantiation
    print("Step 1")
    o1 = SomeClass(11, 22)
    o1.a = 55
    o1.a = 66

    # validated manually
    print("\nStep 2")
    attr.validate(o1)

    # validated every time
    print("\nStep 3")
    o2 = SomeClassB(11)
    o2.a = 77
    o2.a = 88
