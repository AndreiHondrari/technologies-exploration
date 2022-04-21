from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    a: int = attr.field()

    @a.validator
    def check_a(
        inst: "Item",
        prop: attr.Attribute,
        val: int
    ) -> None:
        if val < 0:
            raise ValueError(f"Field 'a' must be positive. {val} is not")


if __name__ == '__main__':
    hprint("Bad init")
    try:
        item = Item(a=-123)  # NOTICE THE MINUS SIGN
        print(item)
    except ValueError as e:
        print("EXC: ", repr(e))

    hprint("Good init")
    item = Item(a=123)
