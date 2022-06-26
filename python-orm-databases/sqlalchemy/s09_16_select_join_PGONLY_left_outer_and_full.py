"""
Attention ! - this is a postgres script
"""

from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String,

    insert, select, delete,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session

hprint = partial(print, " \n#")


Base = declarative_base()


class T1(Base):
    __tablename__ = "t1"

    id = Column(Integer, primary_key=True, nullable=False)

    k = Column(Integer)
    y = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"T1(id={self.id}, k='{self.k}', y={self.y})"
        )


class T2(Base):
    __tablename__ = "t2"

    id = Column(Integer, primary_key=True, nullable=False)

    a = Column(String)
    k = Column(Integer)

    def __repr__(self) -> str:
        return (
            f"T2(id={self.id}, a={self.a}, k={self.k})"
        )


def prepare_database() -> Engine:

    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost/somedb",
        future=True,
    )
    Base.metadata.create_all(engine)
    return engine


def populate_database(engine: Engine) -> None:
    # insert data
    hprint("Add some data")
    T1_VALUES = [
        {'k': 11, 'y': 777},
        {'k': 22, 'y': 888},
        {'k': 33, 'y': 999},
        {'k': 11, 'y': 1010},
        {'k': 66, 'y': 888},
    ]

    T2_VALUES = [
        {'a': 'a', 'k': 55},
        {'a': 'b', 'k': 22},
        {'a': 'c', 'k': 11},
        {'a': 'b', 'k': 77},
        {'a': 'd', 'k': 22},
    ]

    with engine.begin() as conn:
        conn.execute(insert(T1), T1_VALUES)
        conn.execute(insert(T2), T2_VALUES)


def cleanup(engine: Engine) -> None:
    with Session(engine) as session:
        session.execute(delete(T2))
        session.execute(delete(T1))

    T2.__table__.drop(engine)
    T1.__table__.drop(engine)


def main() -> None:

    engine = prepare_database()
    populate_database(engine)

    with Session(engine) as session:
        hprint("Left outer join statement")
        statement = select(T1.k, T1.y, T2.a, T2.k).join(
            T2,
            T1.k == T2.k,
            isouter=True
        )
        print(statement)

        hprint("Left outer join results")
        rows = session.execute(statement)
        for r in rows:
            print(r)

    with Session(engine) as session:
        hprint("Full outer join statement")
        statement = select(T1.k, T1.y, T2.a, T2.k).join(
            T2,
            T1.k == T2.k,
            full=True
        )
        print(statement)

        hprint("Full outer join results")
        rows = session.execute(statement)
        for r in rows:
            print(r)

    cleanup(engine)


if __name__ == "__main__":
    main()
