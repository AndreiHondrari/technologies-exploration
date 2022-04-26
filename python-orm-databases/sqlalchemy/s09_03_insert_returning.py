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
    print("Create engine ...")
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/somedb",
        future=True
    )
    Base.metadata.create_all(engine)
    return engine


def main() -> None:

    # create engine
    engine = prepare_database()

    session = Session(engine)

    # insert data
    print("Add some data to 'item' table ...")

    """
    NOT SUPPORTED BY ALL dialects
    - postgres supports
    - sqlite does not support
    """
    statement = insert(Item).returning(Item.id, Item.title)
    print(" \nSTATEMENT:\n", statement, sep="")

    result = session.execute(
        statement,
        [
            {'title': 'kaboom', 'value': 111},
            {'title': 'gandalf', 'value': 222},
            {'title': 'maximilian', 'value': 333}
        ]
    )

    hprint("Returned at insert")
    for r in result:
        print(r)

    session.close()


if __name__ == "__main__":
    main()
