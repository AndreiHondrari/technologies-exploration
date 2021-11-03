import enum

import attr


@enum.unique
class Category(enum.IntEnum):
    HEAVY = enum.auto()
    MEDIUM = enum.auto()
    LIGHT = enum.auto()


@attr.s(kw_only=True)
class Item:
    value: int = attr.ib()
    name: str = attr.ib()
    category: Category = attr.ib()


if __name__ == '__main__':

    item1 = Item(value=111, name="Maximus", category=Category.HEAVY)

    # premade include filter
    item1_dict = attr.asdict(
        item1,
        filter=attr.filters.include(
            attr.fields(Item).name,
            Category
        )
    )
    print("D1", item1_dict)
