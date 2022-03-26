from functools import partial

from sqlalchemy import (
    MetaData, Table, Column, Integer, String, ForeignKey,
    create_engine,
)

hprint = partial(print, "\n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
    )

    # define data structures
    metadata_obj = MetaData()

    Table(
        "potato", metadata_obj,
        Column('pk', Integer, primary_key=True),
        Column('size', Integer),
    )

    Table(
        "item",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('title', String(30)),
        Column('description', String, nullable=False),
        Column('value', Integer),
        Column('potato', ForeignKey('potato.pk'), nullable=False),
    )

    metadata_obj.create_all(engine)


if __name__ == "__main__":
    main()
