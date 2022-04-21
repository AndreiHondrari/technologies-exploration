from typing import List
from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    x: int = attr.field(default=11)

    # NOT PROPER
    # beware that this is created only once and
    # persists between instances
    # DO NOT USE !
    items: List[int] = attr.field(default=[])

    collection: List[str] = attr.field(default=attr.Factory(list))

    stuff: List[int] = attr.field(factory=list)


if __name__ == '__main__':
    hprint("O1")
    o1 = Item()
    o1.items.append(123)
    print("o1", o1)

    hprint("O2")
    o2 = Item()
    o2.collection.append("blabla")
    print("o2", o2)

    hprint("O3")
    o3 = Item()
    o3.stuff.append(999)
    print("o3", o3)
