import pydantic


class SomeClass(pydantic.BaseModel):
    a: int
    b: int


if __name__ == '__main__':
    try:
        SomeClass(a=11)
    except pydantic.ValidationError as e:

        print("Caugh exception:", repr(e), "\n")

        print("Ex json:", e.json())
