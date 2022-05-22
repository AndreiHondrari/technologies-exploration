import time

from sqlalchemy import create_engine, text


def main() -> None:
    print("Start index creation ...")
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
        with engine.begin() as conn:
            start = time.time()
            conn.execute(
                text("DROP INDEX IF EXISTS idx01")
            )
            stop = time.time()

        elapsed = stop - start

    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    print(f"Index creation DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
