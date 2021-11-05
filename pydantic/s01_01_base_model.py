from pydantic import BaseModel


class SomeClass(BaseModel):
    x: int
    bla: str = "Something"


if __name__ == '__main__':
    o1 = SomeClass(x=11)
    print("o1:", o1)

    print("o1 json:", o1.json())
    print("o1 dict:", o1.dict())
    print("o1 schema:", o1.schema())
