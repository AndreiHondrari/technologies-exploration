import attr


@attr.s(kw_only=True)
class SomeClass:
    a: str = attr.ib(
        converter=attr.converters.default_if_none("")  # type: ignore[misc]
    )


if __name__ == '__main__':
    o1 = SomeClass(a=123)
    print("o1", o1)

    o2 = SomeClass(a=None)
    print("o2", o2)
