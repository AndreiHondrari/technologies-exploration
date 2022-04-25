"""
Assign labels to columns when selecting.
"""

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

    hprint("Get the data")
    statement = select(
        Item.id.label('divine_identity'),
        Item.title.label('given_name'),
        Item.value.label('worthiness'),
    )
    print(statement)

    with Session(engine) as session:
        items = session.execute(statement)
        hprint("Result")
        print("COLUMN_NAMES", items.keys())
        for x in items:
            print(f"{x.divine_identity} | {x.given_name} | {x.worthiness}")


if __name__ == "__main__":
    main()
