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

    hprint("table pk")
    print(item_table.primary_key)

    hprint("columns")
    print(item_table.c)
    print(item_table.columns)
    print(item_table.columns.keys())

    hprint("iterated columns")
    for col in item_table.c:
        print(col, type(col))

    hprint("column details")
    print(item_table.c.title)
    print([x for x in dir(item_table.c.title) if not x.startswith('_')])
    print("TITLE_COLUMN_NAME", item_table.c.title.name)
    print("TITLE_COLUMN_TYPE", item_table.c.title.type)



if __name__ == "__main__":
    main()
