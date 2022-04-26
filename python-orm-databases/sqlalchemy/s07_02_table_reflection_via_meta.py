from pprint import pprint
from functools import partial

from sqlalchemy import (
    create_engine, MetaData, Table,
    text,
)

hprint = partial(print, " \n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
    )

    # NOTICE absence of a primary key
    with engine.connect() as conn:
        conn.execute(text(
            """
            CREATE TABLE item (
                val INTEGER,
                title VARCHAR(30)
            )
            """
        ))

    # init metadata
    metadata = MetaData()

    metadata.reflect(engine)

    item_table = metadata.tables['item']

    hprint("Item table reflected")
    pprint(item_table)


if __name__ == "__main__":
    main()
