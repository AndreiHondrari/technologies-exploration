
from typing import Any, Dict, cast, List

import cattr
from attr import define


@define
class SubItem:
    a: int
    b: int
    c: int
    d: int


@define
class SubItem2:
    f: int
    r: str


@define
class Item:
    x: int
    y: int

    a: int
    b: int
    c: int
    d: int

    descr: str
    descr_a: str
    descr_b: str

    subitem_1: SubItem
    collection: List[SubItem2]
    collection_2: List[str]


def structure(item_dict: Dict[str, Any]) -> Item:
    return cattr.structure(item_dict, Item)


def destructure(item: Item) -> Dict[str, Any]:
    return cast(Dict[str, Any], cattr.unstructure(item))
