import os
from pathlib import Path

from sqlalchemy import create_engine, text


def main() -> None:
    print("Start cleanup ...")
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/somedb",
        echo=True,
        future=True
    )
    print("Create")
    with engine.connect() as conn:

        conn.execute(text("DROP TABLE IF EXISTS test_table_1"))
        conn.commit()

    print("Cleanup DONE")


if __name__ == "__main__":
    main()
