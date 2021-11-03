import attr


def on_set_of_anything(instance, attribute, value) -> None:
    print(f"SET {value} for '{attribute.name}'")


@attr.s(on_setattr=on_set_of_anything)
class SomeClass:
    a: int = attr.ib()
    b: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(11, 22)
    o1.a = 33
    o1.b = 55
