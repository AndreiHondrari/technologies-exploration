from functools import partial

import attr

hprint = partial(print, " \n#")


@attr.define(kw_only=True)
class Item:
    _x: int
    _k: float = attr.field(init=False, default=42)
    t: str


def main() -> None:
    hprint("Trying to init a non-initializable field")
    try:
        item = Item(x=11, k=22.33, t="something")  # type: ignore
    except Exception as exc:
        print("EXC: ", repr(exc))

    hprint("Init normally")
    item = Item(x=11, t="something")
    print(item)


if __name__ == "__main__":
    main()
