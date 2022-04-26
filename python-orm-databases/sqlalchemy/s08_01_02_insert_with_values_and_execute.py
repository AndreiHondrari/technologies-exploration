from functools import partial

from sqlalchemy import (
    create_engine, text,
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
    v = Column(Integer)
    d = Column(String(30))

    def __repr__(self) -> str:
        return (
            f"Item(id={self.id}, v={self.v}), d='{self.d}'"
        )


def prepare_database() -> Engine:

    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True
    )
    Base.metadata.create_all(engine)
    return engine


def main() -> None:
    engine = prepare_database()

    session = Session(engine)

    statement = insert(Item).values([
        {'v': 11, 'd': "onety-one"},
        {'v': 22, 'd': "twenty-two"}
    ])

    # The parameter values will not be used
    session.execute(statement, {'v': 33, 'd': "thirty-three"})
    session.commit()

    items = session.scalars(select(Item))
    for p in items:
        print(p)

    session.close()


if __name__ == "__main__":
    main()
