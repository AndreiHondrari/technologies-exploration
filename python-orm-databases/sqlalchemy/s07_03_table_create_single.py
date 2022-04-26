from functools import partial

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer,
)

hprint = partial(print, " \n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
    )

    # init metadata
    metadata = MetaData()

    # declara table
    item_table = Table("item", metadata, Column('val', Integer))

    item_table.create(engine)
    print(metadata.tables)


if __name__ == "__main__":
    main()
