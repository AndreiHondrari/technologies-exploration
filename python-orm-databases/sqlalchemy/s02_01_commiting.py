"""
- create a table with execute and then commit
- insert some values in the new table
- ROLLBACK is not issue because of the commit
- select rows from the previously created table
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
        conn.execute(text("INSERT INTO mytable VALUES (10, 'HEY')"))
        conn.commit()

    hprint("Select")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM mytable"))
        print(result.all())


if __name__ == "__main__":
    main()
