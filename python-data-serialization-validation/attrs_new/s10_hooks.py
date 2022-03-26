import attr


@attr.define
class Item:
    a: int = attr.ib()

    def __attrs_pre_init__(self) -> None:
        print("PRE_INIT")

    def __init__(self, a: int) -> None:
        print("BEF_INIT", flush=True)
        self.__attrs_init__(a)
        print("AFT_INIT", flush=True)

    def __attrs_post_init__(self) -> None:
        print("POST_INIT")


if __name__ == '__main__':
    item = Item(123)
    print(item)
