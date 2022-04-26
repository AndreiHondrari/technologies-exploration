from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String,

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


def prepare_database() -> Engine:
    print("Create engine ...")
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True,
    )
    Base.metadata.create_all(engine)
    return engine


def populate_database(engine: Engine) -> None:
    # insert data
    print("Add some data ...")
    with engine.begin() as conn:
        conn.execute(
            insert(Item.__table__),
            [
                {'title': 'kaboom', 'value': 111},
                {'title': 'traktor', 'value': 222},
            ]
        )


def main() -> None:

    engine = prepare_database()
    populate_database(engine)

    session = Session(engine)

    hprint("Insert from select in 'something_else' table")
    items_select = select(Item.title + "-san", Item.value)
    insert_statement = insert(SomethingElse).from_select(
        ["name", "worth"], items_select
    )

    print("\nSTATEMENT:\n", insert_statement, "\n", sep="")

    session.execute(insert_statement)
    session.commit()

    rows = session.execute(select(SomethingElse))
    for r in rows:
        print(r)

    session.close()


if __name__ == "__main__":
    main()
