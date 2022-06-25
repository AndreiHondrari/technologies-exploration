"""
Notice that the other side of the join is automatically inferred.
"""
import random
from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String, ForeignKey,

    insert, select,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session

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


class Potato(Base):
    __tablename__ = "potato"

    pk = Column(Integer, primary_key=True)

    name = Column(String(30))
    worth = Column(Integer)

    item_id = Column(ForeignKey('item.id'))

    def __repr__(self) -> str:
        return (
            f"Potato(pk={self.pk}, "
            f"name='{self.name}', worth={self.worth}, item_id={self.item_id})"
        )


def prepare_database() -> Engine:

    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
    )
    Base.metadata.create_all(engine)
    return engine


def populate_database(engine: Engine) -> None:
    # insert data
    hprint("Add some data")
    ITEM_VALUES = [
        {
            'title': f"kaboom-{i}-{random.randint(100, 1_000)}",
            'value': i
        }
        for i in range(10)
    ]

    POTATO_VALUES = [
        {
            'name': f"bulba-{i}",
            'worth': i * 11,
            'item_id': 5,
        }
        for i in range(5)
    ]

    with engine.begin() as conn:
        conn.execute(insert(Item), ITEM_VALUES)
        conn.execute(insert(Potato), POTATO_VALUES)


def main() -> None:

    engine = prepare_database()
    populate_database(engine)

    hprint("JOIN ITEM")
    statement = select(Item, Potato).join(Item)
    print(statement)

    hprint("JOIN POTATO")
    statement = select(Item, Potato).join(Potato)
    print(statement)

    hprint("Get the data")
    with Session(engine) as session:
        items = session.execute(statement)
        for x in items:
            print(x)


if __name__ == "__main__":
    main()
