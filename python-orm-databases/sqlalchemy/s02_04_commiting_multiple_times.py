"""
- pass multiple rows for insertion using a list of dictionaries
"""
from functools import partial

from sqlalchemy import create_engine, text

hprint = partial(print, " \n#")


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

    hprint("Insert")
    with engine.connect() as conn:
        print("two inserts")
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            {'x': 11, 'd': 'abacus'}
        )
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            {'x': 22, 'd': 'sorcerer'}
        )

        print("first commit")
        conn.commit()

        print("some bad insert")

        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            {'x': 999999, 'd': '!!!___THIS_IS_BAD___!!!'}
        )

        print("rollback bad insert")
        conn.rollback()

        print("more inserts")
        conn.execute(
            text("INSERT INTO mytable VALUES (:x, :d)"),
            [
                {'x': 33, 'd': 'gandalf'},
                {'x': 44, 'd': 'magnus'},
                {'x': 55, 'd': 'maximilian'},
            ]
        )

        print("another commit")
        conn.commit()

        print("try rollback")
        conn.rollback()

    hprint("Select")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM mytable"))
        print(result.all())


if __name__ == "__main__":
    main()
