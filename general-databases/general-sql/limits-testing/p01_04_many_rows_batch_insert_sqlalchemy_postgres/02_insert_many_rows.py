import time
import random

from functools import partial

from sqlalchemy import create_engine, text

hprint = partial(print, "\n#")


def main() -> None:
    print("Start values generation")
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/somedb",
        echo=True,
        future=True,
        executemany_mode='values',
        executemany_values_page_size=100_000
    )

    print("Generating values list ...")
    values = []

    for i in range(10_000_000):
        val = random.randint(100, 1_000)
        values.append({'_id': i, 'val': val})

    start = time.time()

    try:
        print("Executing in batch ... (probably 120 seconds)")
        with engine.begin() as conn:
            conn.execute(
                text("INSERT INTO test_table_1 VALUES (:_id, :val)"),
                values
            )

        stop = time.time()
        elapsed = stop - start
    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    print(f"Values generation DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
