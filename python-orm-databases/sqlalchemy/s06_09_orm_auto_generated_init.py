from functools import partial

from sqlalchemy import (
    Column, Integer, String,
)
from sqlalchemy.orm import declarative_base

hprint = partial(print, " \n#")


def main() -> None:
    Base = declarative_base()

    class Item(Base):
        __tablename__ = "item"

        id = Column(Integer, primary_key=True, nullable=False)
        title = Column(String(30))
        description = Column(String, nullable=False)
        value = Column(Integer)

        def __repr__(self) -> str:
            return (
                f"Item(id={self.id}, title='{self.title}', value={self.value})"
            )

    item_1 = Item(title="Something", value=111)
    item_2 = Item(title="SomeElse", value=222)

    print(repr(item_1))
    print(repr(item_2))


if __name__ == "__main__":
    main()
