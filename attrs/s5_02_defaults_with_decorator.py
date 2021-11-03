import attr


@attr.s(kw_only=True)
class SomeClass:
    a: int = attr.ib()
    b: int = attr.ib()

    @b.default
    def _y_default(self) -> int:
        return self.a * 2


if __name__ == '__main__':
    o1 = SomeClass(a=11)
    print("o1", o1)
