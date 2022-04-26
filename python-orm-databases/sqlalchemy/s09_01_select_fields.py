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

    # Core table
    hprint("(fields) from the core table")
    result = session.execute(
        select(Item.__table__.c.id, Item.__table__.c.title)
    )
    for x in result:
        print(x)

    # ORM model
    hprint("(fields) from the ORM table")
    result = session.execute(
        select(Item.id, Item.title)
    )
    for x in result:
        print(x)

    session.close()


if __name__ == "__main__":
    main()
