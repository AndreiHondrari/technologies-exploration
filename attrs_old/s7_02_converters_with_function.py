import attr


def convert_value(value: int) -> int:
    return value * 2


@attr.s(kw_only=True)
class SomeClass:
    a: int = attr.ib(converter=convert_value)


if __name__ == '__main__':
    o1 = SomeClass(a=111)
    print("o1", o1)
