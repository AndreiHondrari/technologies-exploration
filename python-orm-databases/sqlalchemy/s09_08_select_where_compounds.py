import random
from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String,

    insert, select, and_, or_
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
    VALUES = [
        {
            'title': f"kaboom-{i}-{random.randint(100, 1_000)}",
            'value': i
        }
        for i in range(100)
    ]

    with engine.begin() as conn:
        conn.execute(insert(Item.__table__), VALUES)


def main() -> None:

    engine = prepare_database()
    populate_database(engine)

    hprint("Get the data")
    statement = select(Item).where(
        and_(
            or_(
                Item.value == 1,
                Item.value < 5,
                Item.value > 95,
            ),
            Item.value % 2 == 1
        )
    )
    print(statement)

    with Session(engine) as session:
        items = session.scalars(statement)
        for x in items:
            print(x)


if __name__ == "__main__":
    main()
