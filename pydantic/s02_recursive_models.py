from typing import List
from pydantic import BaseModel


class SomeSubclass(BaseModel):
    a: int
    b: int


class SomeSubclassB(BaseModel):
    bla: str


class SomeClass(BaseModel):
    x: int
    p: SomeSubclass
    q: List[SomeSubclassB]


if __name__ == '__main__':
    x1 = SomeSubclass(a=77, b=88)
    l1 = [
        SomeSubclassB(bla="foo"),
        SomeSubclassB(bla="bar"),
    ]
    o1 = SomeClass(x=11, p=x1, q=l1)
    print("o1:", o1)
