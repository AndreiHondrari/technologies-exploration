import attr


@attr.s(kw_only=True)
class Item:
    x: int = attr.ib(kw_only=True)
    y: int = attr.ib(kw_only=True)


if __name__ == '__main__':
    item1 = Item(x=11, y=22)

    # lambda filter
    item1_dict = attr.asdict(
        item1,
        filter=lambda field, value: field.name != "y"
    )
    print("D1", item1_dict)

    # premade exclude filter
    item1_dict_2 = attr.asdict(
        item1,
        filter=attr.filters.exclude(attr.fields(Item).x)
    )
    print("D2", item1_dict_2)
