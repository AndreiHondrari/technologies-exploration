from typing import Any

import attr


def is_positive(
    inst: Any,
    prop: attr.Attribute,
    val: int
) -> None:
    if val < 0:
        raise ValueError(f"Value must be positive. {val} is not")


def is_not_333(
    inst: Any,
    prop: attr.Attribute,
    val: int
) -> None:
    if val == 333:
        raise ValueError("Must not be 333")


@attr.s
class SomeClass:
    a: int = attr.ib(validator=[is_positive, is_not_333])


if __name__ == '__main__':
    try:
        o1 = SomeClass(-111)
        print("o1", o1)
    except ValueError as e:
        print("Caught exception: ", e)

    try:
        o2 = SomeClass(333)
        print("o2", o2)
    except ValueError as e:
        print("Caught exception: ", e)

    o3 = SomeClass(444)
    print("o3", o3)
