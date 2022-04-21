from sqlalchemy import create_engine, text


def main() -> None:
    print("Start setup ...")
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/somedb",
        echo=True,
        future=True
    )
    print("Create")
    with engine.connect() as conn:

        conn.execute(text("DROP TABLE IF EXISTS test_table_1"))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS test_table_1 (
            id INTEGER,
            val INTEGER,

            PRIMARY KEY (id)
        )
        """))

        conn.commit()

    print("Setup DONE")


if __name__ == "__main__":
    main()
