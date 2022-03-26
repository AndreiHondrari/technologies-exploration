from functools import partial

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

hprint = partial(print, "\n#")


def main() -> None:

    metadata_obj = MetaData()

    Table(
        "potatoes", metadata_obj,
        Column('pk', Integer, primary_key=True),
        Column('size', Integer),
    )

    Table(
        "item",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('title', String(30)),
        Column('description', String),
        Column('potato', ForeignKey('potatoes.pk'), nullable=False),
    )


if __name__ == "__main__":
    main()
