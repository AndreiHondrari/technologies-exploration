from pprint import pprint
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
    kek_table = Table("kek", metadata, Column('bla', Integer))

    hprint("Create tables")
    item_table.create(engine)
    kek_table.create(engine)
    pprint(metadata.tables)

    hprint("Drop table (item)")
    item_table.drop(engine)
    pprint(metadata.tables)  # NOTICE item stil in tables

    hprint("Update metadata")
    metadata.remove(item_table)
    pprint(metadata.tables)


if __name__ == "__main__":
    main()
