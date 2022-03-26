import attr


@attr.define
class Item:
    x: int
    k: float
    t: str


def main() -> None:
    item = Item(10, 26.89, "blabla")
    print(item)


if __name__ == "__main__":
    main()
