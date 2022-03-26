from functools import partial
from typing import Dict, Any

import attr
import cattr

hprint = partial(print, "\n#")


@attr.define
class Item:
    x: int
    c: float
    t: str


def main() -> None:
    item1 = Item(x=11, c=55.78, t="kartof")
    result: Dict[str, Any] = cattr.unstructure(item1)
    print(result)


if __name__ == "__main__":
    main()
