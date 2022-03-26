
from typing import Any, Dict, List

from pydantic import BaseModel


class SubItem(BaseModel):
    a: int
    b: int
    c: int
    d: int


class SubItem2(BaseModel):
    f: int
    r: str


class Item(BaseModel):
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
    return Item(**item_dict)


def destructure(item: Item) -> Dict[str, Any]:
    return item.dict()
