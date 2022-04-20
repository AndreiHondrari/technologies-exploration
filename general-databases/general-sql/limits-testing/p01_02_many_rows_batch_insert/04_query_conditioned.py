import time

import psycopg2 as pg


def main() -> None:
    print("Start query for all")

    # setup
    conn = pg.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        database="somedb"
    )
    curr = conn.cursor()

    # main
    start = time.time()

    try:
        print("Querying ...")
        curr.execute(
            "SELECT * FROM test_table_1 WHERE val = 100"
        )

        stop = time.time()
        elapsed = stop - start

        results = curr.fetchall()
        print("No of rows:", len(results))

    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
        elapsed = 0

    # cleanup
    curr.close()
    conn.close()
    print(f"Query DONE ({elapsed:.2f}s)")


if __name__ == "__main__":
    main()
