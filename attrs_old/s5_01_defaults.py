from typing import List

import attr


@attr.s
class SomeClass:
    x: int = attr.ib(default=11)

    # NOT PROPER
    # beware that this is created only once and
    # persists between instances
    # DO NOT USE !
    items: List[int] = attr.ib(default=[])

    collection: List[str] = attr.ib(default=attr.Factory(list))

    stuff: List[int] = attr.ib(factory=list)


if __name__ == '__main__':
    o1 = SomeClass()
    o1.items.append(123)
    print("o1", o1)

    o2 = SomeClass()
    o2.collection.append("blabla")
    print("o2", o2)

    o3 = SomeClass()
    o3.stuff.append(999)
    print("o3", o3)
