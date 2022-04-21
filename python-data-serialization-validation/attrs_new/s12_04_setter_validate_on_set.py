from functools import partial

import attr

hprint = partial(print, " \n#")


def validate_a(instance, attribute, value) -> None:
    print("VALIDATING:", attribute.name, value)


@attr.define(kw_only=True)
class ItemX:
    a: int = attr.field(validator=validate_a)
    b: int = attr.field()


@attr.define(kw_only=True)
class ItemY:
    a: int = attr.field(
        validator=validate_a,

        # seems that validators are called by default so here we inhibit
        on_setattr=attr.setters.NO_OP
    )


if __name__ == '__main__':
    hprint("Change for ItemX.a")
    x_item = ItemX(a=11, b=22)
    x_item.a = 99

    hprint("Change for ItemY.a")
    y_item = ItemY(a=11)
    y_item.a = 77
