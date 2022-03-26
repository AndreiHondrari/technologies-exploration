from functools import partial

from sqlalchemy import MetaData, Table, Column, Integer, String

hprint = partial(print, "\n#")


def main() -> None:

    metadata_obj = MetaData()

    Table(
        "item", metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('title', String(30)),
        Column('description', String),
    )

    Table(
        "potatoes", metadata_obj,
        Column('pk', Integer, primary_key=True),
        Column('size', Integer),
    )

    Table(
        "achievements", metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('kind', Integer),
    )

    hprint("metadata")
    print(metadata_obj)
    print("TABLE_KEYS", metadata_obj.tables.keys())
    print("INFO", metadata_obj.info)

    hprint("tables from metadata")
    for table in metadata_obj.sorted_tables:
        print(table.name)


if __name__ == "__main__":
    main()
