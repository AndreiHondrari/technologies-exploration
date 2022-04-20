import psycopg2 as pg


CLEANUP_SQL = """
DROP TABLE IF EXISTS test_table_1;
"""


def main() -> None:
    print("Starting cleanup ...")
    conn = pg.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        database="somedb"
    )
    curr = conn.cursor()

    curr.execute(CLEANUP_SQL)
    conn.commit()

    curr.close()
    conn.close()
    print("Cleanup DONE")


if __name__ == "__main__":
    main()
