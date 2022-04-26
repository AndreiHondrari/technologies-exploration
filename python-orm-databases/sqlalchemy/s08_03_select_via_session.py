"""
Notice that when using Session.execute(select(Model)) the rows are actually
tuples of a single element, containing the actual entity returned from
the database.

If instead you use Session.execute(select(Model.field1, Model.field2))
the fields are mapped as elements of the tuple.
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

    session = Session(engine)

    # Core table
    hprint("From the core table")

    statement = select(Item.__table__)  # notice select on Table
    result = session.execute(statement)  # ! returns a CursorResult

    print("STATEMENT:", statement)
    print("RESULT_TYPE", type(result))

    print("\nCore select results")
    for x in result:
        print(type(x), x)

    # ORM model
    hprint("From the ORM table")

    statement = select(Item)  # Notice select on table model
    result = session.execute(statement)  # ! returns a ChunkedIteratorResult

    print("STATEMENT:", statement)
    print("RESULT_TYPE", type(result))

    print("\nORM select results")
    for x in result:
        print(type(x), x)

    session.close()


if __name__ == "__main__":
    main()
