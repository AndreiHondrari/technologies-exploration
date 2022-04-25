from functools import partial

from sqlalchemy import (
    create_engine, MetaData, Table,
    Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import registry

hprint = partial(print, " \n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
    )

    # declare base registry
    mapper_registry = registry()
    Base = mapper_registry.generate_base()

    # init metadata
    metadata = MetaData()

    # declara table
    item_table = Table(
        "item",
        metadata,
        Column('id', Integer, primary_key=True, nullable=False),
        Column('title', String(30)),
        Column('value', Integer)
    )

    # define table
    class Item(Base):
        __table__ = item_table

        def __repr__(self) -> str:
            return (
                f"Item(id={self.id}, title='{self.title}', value={self.value})"
            )

    hprint("Emit DDL")
    metadata.create_all(engine)


if __name__ == "__main__":
    main()
