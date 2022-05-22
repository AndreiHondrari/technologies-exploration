import time

from sqlalchemy import create_engine, text


def main() -> None:
    print("Start query conditioned ...")
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/somedb",
        echo=True,
        future=True
    )

    start: float = 0
    stop: float = 0
    elapsed: float = 0

    try:
        print("Querying ...")
        with engine.connect() as conn:
            start = time.time()
            results = conn.execute(
                text("SELECT * FROM test_table_2 WHERE val = :val"),
                {'val': 9999}
            ).all()
            stop = time.time()
            print("No of rows:", len(results))

        elapsed = stop - start

    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    print(f"Query DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
