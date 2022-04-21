"""
- proove that you can not do SQL injection because of text()
"""

import logging

from functools import partial

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

hprint = partial(print, " \n#")


def prepare_database(engine: Engine) -> None:
    with engine.begin() as conn:
        # create table
        conn.execute(text("CREATE TABLE mytable (x int, d varchar(250))"))

        # insert data
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            [
                {'x': 10, 'd': "AAA"},
                {'x': 20, 'd': "BBB"},
                {'x': 30, 'd': "CCC"},
                {'x': 40, 'd': "DDD"},
                {'x': 50, 'd': "EEE"},
            ]
        )


def main() -> None:

    # initialize
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True
    )

    logging.disable(logging.WARNING)

    # populate
    prepare_database(engine)

    logging.disable(0)

    hprint("Injection")
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT * FROM mytable WHERE x > :x_low"),
            {'x_low': "30; DROP TABLE mytable"}
        )
        # conn.execute(text("DROP TABLE mytable"))

    hprint("Select final")
    with engine.begin() as conn:
        result = conn.execute(text("SELECT * FROM mytable"))
        for row in result:
            print(row)


if __name__ == "__main__":
    main()
