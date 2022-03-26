from functools import partial
from typing import List

from pydantic import BaseModel

hprint = partial(print, "\n#")


class SubItemA(BaseModel):
    a: int
    b: int


class SubItemB(BaseModel):
    bla: str


class Item(BaseModel):
    x: int
    p: SubItemA
    q: List[SubItemB]


if __name__ == '__main__':
    x1 = SubItemA(a=77, b=88)

    l1 = [
        SubItemB(bla="foo"),
        SubItemB(bla="bar"),
    ]

    hprint("Item")
    item = Item(x=11, p=x1, q=l1)
    print(item)
