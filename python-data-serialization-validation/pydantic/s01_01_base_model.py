from functools import partial

from pydantic import BaseModel

hprint = partial(print, " \n#")


class Item(BaseModel):
    x: int
    bla: str = "Something"


if __name__ == '__main__':
    item = Item(x=11)
    hprint("Our object")
    print("item:", item)

    hprint("To JSON")
    print(item.json())

    hprint("To dict")
    print(item.dict())

    hprint("Schema")
    print(item.schema())
