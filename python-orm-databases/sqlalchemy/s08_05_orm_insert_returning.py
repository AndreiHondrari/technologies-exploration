"""
WARNING - This sample does not work

RETURNING is not supported fully yet by all dialects and operations.
"""

from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String,

    insert, select,
)
from sqlalchemy.orm import declarative_base

hprint = partial(print, " \n#")


Base = declarative_base()


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(30))
    value = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"Item(id={self.id}, title='{self.title}', value={self.value})"
        )


def main() -> None:

    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
    )
    Base.metadata.create_all(engine)

    # insert data
    hprint("Add some data to 'item' table")
    with engine.begin() as conn:
        result = conn.execute(
            insert(Item).returning(Item.id, Item.title),
            {'title': 'kaboom', 'value': 111}
        )

        for r in result:
            print(r)


if __name__ == "__main__":
    main()
