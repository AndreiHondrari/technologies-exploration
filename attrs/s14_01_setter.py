import attr


def on_set_of_a(instance, attribute, value) -> None:
    print(f"SET {value} for '{attribute.name}'")


@attr.s
class SomeClass:
    a: int = attr.ib(on_setattr=on_set_of_a)
    b: int = attr.ib()


if __name__ == '__main__':
    o1 = SomeClass(11, 22)
    o1.a = 33
