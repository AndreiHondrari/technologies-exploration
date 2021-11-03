import attr


@attr.s
class SomeClass:
    a: int = attr.ib()

    def __attrs_pre_init__(self) -> None:
        print("PRE_INIT")

    def __attrs_post_init__(self) -> None:
        print("POST_INIT")


if __name__ == '__main__':
    o1 = SomeClass(123)
    print("o1", o1)
