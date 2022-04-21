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


class SomethingElse(Base):
    __tablename__ = "something_else"

    pk = Column(Integer, primary_key=True)

    name = Column(String(30))
    worth = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"SomethingElse(pk={self.pk}, "
            f"name='{self.name}', worth={self.worth})"
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
        conn.execute(
            insert(Item.__table__),
            [
                {'title': 'kaboom', 'value': 111},
                {'title': 'traktor', 'value': 222},
            ]
        )
        rows = conn.execute(select(Item))
        for r in rows:
            print(r)

    hprint("Insert from select in 'something_else' table")
    items_select = select(Item.title + "-san", Item.value)
    insert_statement = insert(SomethingElse).from_select(
        ["name", "worth"], items_select
    )
    with engine.connect() as conn:
        conn.execute(insert_statement)

        rows = conn.execute(select(SomethingElse))
        for r in rows:
            print(r)


if __name__ == "__main__":
    main()
