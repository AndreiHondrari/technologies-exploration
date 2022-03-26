"""
- pass multiple rows for insertion using a list of dictionaries
"""
from functools import partial

from sqlalchemy import create_engine, text

hprint = partial(print, "\n#")


def main() -> None:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True
    )
    hprint("Create")
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE mytable (x int, d varchar(250))"))
        conn.commit()

    hprint("First autocommit insert")
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            [
                {'x': 11, 'd': "Ergo sum est retrostylus"},
                {'x': 33, 'd': "Duis incididunt laborum tempor aliquip."},
                {'x': 99, 'd': "Qui ex deserunt occaecat consectetur magna."},
            ]
        )

    hprint("Additional insertion")
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            [
                {'x': 555, 'd': "AAA"},
                {'x': 666, 'd': "BBB."},
                {'x': 777, 'd': "CCC"},
            ]
        )

    hprint("Select")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM mytable"))
        print(result.all())


if __name__ == "__main__":
    main()
