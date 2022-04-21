"""
- store an SQL statement in a variable, and bind parameters to it
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

    hprint("Save the statement")
    a_statement = text(
        "SELECT * FROM mytable WHERE x > :x_low"
    ).bindparams(x_low=30)

    hprint("Select")
    with engine.connect() as conn:
        result = conn.execute(a_statement)

        for row in result:
            print(row)

    hprint("Select AGAIN")
    with engine.connect() as conn:
        result = conn.execute(a_statement)

        for row in result:
            print(row)


if __name__ == "__main__":
    main()
