import attr


def double_value(value: int) -> int:
    return value * 2


def multiply_by_10(value: int) -> int:
    return value * 10


@attr.s(kw_only=True)
class SomeClass:
    a: int = attr.ib(
        converter=attr.converters.pipe(  # type: ignore
            double_value, multiply_by_10
        )
    )

    b: int = attr.ib(
        converter=[double_value, multiply_by_10]  # type: ignore
    )


if __name__ == '__main__':
    o1 = SomeClass(a=111, b=77)
    print("o1", o1)
