from functools import partial

from pydantic import BaseModel

hprint = partial(print, " \n#")


class Item(BaseModel):
    x: int
    bla: str = "Something"


if __name__ == '__main__':
    d1 = {'x': 22}

    hprint("Create from dictionary")
    o1 = Item(**d1)
    print(o1)

    hprint("Parse dictionary")
    o2 = Item.parse_obj(d1)
    print(o2)
