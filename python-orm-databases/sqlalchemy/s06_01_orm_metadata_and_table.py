import pprint

from functools import partial

from sqlalchemy import MetaData, Table, Column, Integer, String

hprint = partial(print, "\n#")


def main() -> None:

    metadata_obj = MetaData()

    item_table = Table(
        "item",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('title', String(30)),
        Column('description', String),
    )

    hprint("item table attributes")
    pprint.pprint([x for x in dir(item_table) if not x.startswith('_')])

    hprint("metadata")
    print(metadata_obj)
    pprint.pprint([x for x in dir(metadata_obj) if not x.startswith('_')])


if __name__ == "__main__":
    main()
