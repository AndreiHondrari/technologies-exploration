
import dataclasses as dc
from typing import Any, Dict, cast, List

from rest_framework import serializers


@dc.dataclass
class SubItem:
    a: int
    b: int
    c: int
    d: int


@dc.dataclass
class SubItem2:
    f: int
    r: str


@dc.dataclass
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


class SubItemSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField()
    d = serializers.IntegerField()

    def create(self, validated_data: Dict[str, Any]) -> SubItem:
        return SubItem(**validated_data)


class SubItem2Serializer(serializers.Serializer):
    f = serializers.IntegerField()
    r = serializers.CharField()

    def create(self, validated_data: Dict[str, Any]) -> SubItem2:
        return SubItem2(**validated_data)


class ItemSerializer(serializers.Serializer):
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField()
    d = serializers.IntegerField()

    descr = serializers.CharField()
    descr_a = serializers.CharField()
    descr_b = serializers.CharField()

    subitem_1 = SubItemSerializer()
    collection = SubItem2Serializer(many=True)
    collection_2 = serializers.ListField(
       child=serializers.CharField()
    )

    def create(self, validated_data: Dict[str, Any]) -> Item:
        return Item(**validated_data)


def structure(item_dict: Dict[str, Any]) -> Item:
    serializer = ItemSerializer(data=item_dict)
    serializer.is_valid()
    return cast(Item, serializer.save())


def destructure(item: Item) -> Dict[str, Any]:
    serializer = ItemSerializer(item)
    return cast(Dict[str, Any], serializer.data)
