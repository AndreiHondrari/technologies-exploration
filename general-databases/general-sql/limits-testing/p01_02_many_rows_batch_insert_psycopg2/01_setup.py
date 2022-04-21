import psycopg2 as pg


SETUP_SQL = """
DROP TABLE IF EXISTS test_table_1;

CREATE TABLE IF NOT EXISTS test_table_1 (
    id INTEGER,
    val INTEGER,

    PRIMARY KEY (id)
);
"""


def main() -> None:
    print("Starting setup ...")
    conn = pg.connect(
        host="127.0.0.1",
        user="postgres",
        password="postgres",
        database="somedb"
    )
    curr = conn.cursor()

    curr.execute(SETUP_SQL)
    conn.commit()

    curr.close()
    conn.close()

    print("Setup DONE")


if __name__ == "__main__":
    main()
