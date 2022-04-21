from functools import partial

import pydantic

hprint = partial(print, " \n#")


class Item(pydantic.BaseModel):
    a: int
    b: int


if __name__ == '__main__':
    hprint("Missing value validation")
    try:
        Item(a=11)
    except pydantic.ValidationError as e:
        print("Caugh exception:", repr(e), "\n")
        print("Ex json:", e.json())

    hprint("Wrong value type validation")
    try:
        Item(a=11, b="potato")
    except pydantic.ValidationError as e:
        print("Caugh exception:", repr(e), "\n")
        print("Ex json:", e.json())
