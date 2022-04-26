from pprint import pprint
from functools import partial

from sqlalchemy import (
    create_engine, text,
)

hprint = partial(print, " \n#")


def main() -> None:
    # create engine
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True
    )

    con = engine.connect()

    # create the table
    con.execute(text("CREATE TABLE t1 (x int, d text)"))
    con.commit()

    # declare a bound statement
    some_statement = text(
        "INSERT INTO t1 VALUES (:x, :d)"
    ).bindparams(x=111, d="gandalf")

    # use the bound statement multiple times
    for i in range(3):
        con.execute(some_statement)

    con.commit()

    hprint("Results")
    results = con.execute(text("SELECT * FROM t1")).all()
    for r in results:
        print(r)

    con.close()


if __name__ == "__main__":
    main()
