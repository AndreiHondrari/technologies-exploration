import time

from sqlalchemy import create_engine, text


def main() -> None:
    print("Start query conditioned ...")
    engine = create_engine(
        "sqlite+pysqlite:///db.sqlite3",
        echo=True,
        future=True
    )

    start = time.time()

    try:
        print("Querying ...")
        with engine.connect() as conn:
            results = conn.execute(
                text("SELECT * FROM test_table_1 WHERE val = 100")
            ).all()
            print("No of rows:", len(results))

        stop = time.time()
        elapsed = stop - start

    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    print(f"Query DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
