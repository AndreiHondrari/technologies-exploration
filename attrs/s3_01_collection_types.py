import attr


@attr.s(kw_only=True)
class Item:
    x: int = attr.ib(kw_only=True)
    y: int = attr.ib(kw_only=True)


if __name__ == '__main__':

    item1 = Item(x=11, y=22)
    item1_dict = attr.asdict(item1)
    print(item1_dict)
