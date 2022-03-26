"""

- use create_engine to create a database engine
- use engine.connect() to create a connection in a with block
- execute an SQL statement on the resulting connection object

Observations:
- at the end of an engine.connect block, a ROLLBACK will be
  automatically issued
- text function is used to curate the SQL (against SQL injection)
"""
from sqlalchemy import create_engine, text


def main() -> None:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        echo=True,
        future=True
    )

    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


if __name__ == "__main__":
    main()
