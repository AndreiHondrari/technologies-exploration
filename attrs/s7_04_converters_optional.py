from typing import Optional

import attr


@attr.s(kw_only=True)
class SomeClass:
    a: Optional[str] = attr.ib(
        converter=attr.converters.optional(str)
    )


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1)

    o2 = SomeClass(a=None)
    print("o2", o2)
