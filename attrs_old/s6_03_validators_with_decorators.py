from typing import Any

import attr


@attr.s
class SomeClass:
    a: int = attr.ib()

    @a.validator
    def check_a(
        inst: Any,
        prop: attr.Attribute,
        val: int
    ) -> None:
        if val < 0:
            raise ValueError(f"Field 'a' must be positive. {val} is not")


if __name__ == '__main__':
    try:
        o1 = SomeClass(-111)
        print("o1", o1)
    except ValueError as e:
        print("Caught exception: ", e)

    o2 = SomeClass(222)
    print("o2", o2)
