
from functools import partial

from sqlalchemy import (
    create_engine,
    Column, Integer, String,

    select, update, delete,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, Session

hprint = partial(print, " \n#")


Base = declarative_base()


class T1(Base):
    __tablename__ = "t1"

    id = Column(Integer, primary_key=True, nullable=False)

    k = Column(Integer)
    bla = Column(String)

    def __repr__(self) -> str:
        return f"T1(id={self.id}, k={self.k}, bla={self.bla})"


def prepare_database() -> Engine:

    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        future=True
    )
    Base.metadata.create_all(engine)
    return engine


def main() -> None:
    engine = prepare_database()

    print("Create some objects ...")
    o1 = T1(k=11, bla="gandalf")
    o2 = T1(k=22, bla="jeff")
    o3 = T1(k=33, bla="leonardus")
    o4 = T1(k=44, bla="pterodactilus")

    print("Submit objects to database ...")
    # Notice the expire_on_commit
    # which forces the session to not expire our instances.
    # Expired instances can no longer be used after a session
    with Session(engine, expire_on_commit=False) as session:
        session.add(o1)
        session.add(o2)
        session.add_all([o3, o4])
        session.commit()

    hprint("Retrieve all")
    with Session(engine) as session:
        statement = select(T1)
        result = session.execute(statement)
        for x in result.scalars():
            print(x)

    hprint("Retrieve specific")
    with Session(engine) as session:
        statement = select(T1).where(T1.id == o4.id)
        result = session.execute(statement)
        for x in result.scalars():
            print(x)


if __name__ == "__main__":
    main()
