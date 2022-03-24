from typing import List

import attr


@attr.s(kw_only=True)
class Item:
    x: int = attr.ib(kw_only=True)
    y: int = attr.ib(kw_only=True)


@attr.s(kw_only=True)
class Compound:
    items: List[Item] = attr.ib()


if __name__ == '__main__':

    comp1 = Compound(
        items=[
            Item(x=10, y=11),
            Item(x=20, y=22),
            Item(x=30, y=33),
            Item(x=40, y=44),
        ]
    )

    comp1_dict = attr.asdict(comp1)

    print(comp1_dict)
