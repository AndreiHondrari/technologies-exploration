import time
import random

import psycopg2 as pg


SETUP_SQL = """
DROP TABLE IF EXISTS test_table_0;

CREATE TABLE IF NOT EXISTS test_table_0 (
    id INTEGER,
    val INTEGER,

    PRIMARY KEY (id)
);
"""

CLEANUP_SQL = """
DROP TABLE IF EXISTS test_table_0;
"""


def main() -> None:
    print("Start values generation")
    # setup
    conn = pg.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        database="somedb"
    )
    curr = conn.cursor()

    # main
    curr.execute(SETUP_SQL)

    try:
        start = time.time()

        k = 0
        q = 0
        for i in range(5_000):
            val = random.randint(100, 1_000)
            curr.execute(f"INSERT INTO test_table_0 VALUES ({i}, {val})")

            k += 1
            if k % 1000 == 0:
                q += 1000
                print(q)
                k = 0

        print("Committing ...")
        conn.commit()

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    stop = time.time()
    elapsed = stop - start

    # cleanup
    curr.execute(CLEANUP_SQL)
    conn.commit()

    curr.close()
    conn.close()
    print(f"Values generation DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
