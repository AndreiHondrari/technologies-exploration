from pydantic import BaseModel


class SomeClass(BaseModel):
    x: int
    bla: str = "Something"


if __name__ == '__main__':
    d1 = {'x': 22}

    o1 = SomeClass(**d1)
    print("o1:", o1)

    o2 = SomeClass.parse_obj(d1)
    print("o2:", o2)
