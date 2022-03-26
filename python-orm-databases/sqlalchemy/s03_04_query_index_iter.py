"""
- access columns on each row with indexes
"""

from functools import partial

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

hprint = partial(print, "\n#")


def prepare_database(engine: Engine) -> None:
    with engine.begin() as conn:
        # create table
        conn.execute(text("CREATE TABLE mytable (x int, d varchar(250))"))

        # insert data
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            [
                {'x': 555, 'd': "AAA"},
                {'x': 666, 'd': "BBB"},
                {'x': 777, 'd': "CCC"},
            ]
        )


def main() -> None:
    # initialize
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True
    )

    # populate
    prepare_database(engine)

    hprint("Select")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM mytable"))

        for row in result:
            print('\n', '-' * 20, sep='')
            print("X", row[0])
            print("D", row[1])


if __name__ == "__main__":
    main()
