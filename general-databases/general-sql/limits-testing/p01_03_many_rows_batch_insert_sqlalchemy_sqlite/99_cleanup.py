import os
from pathlib import Path

DB_FILENAME = "db.sqlite3"


def main() -> None:
    print("Start cleanup ...")
    print("Cleanup ...")
    db_path = Path(DB_FILENAME).absolute()

    if not db_path.exists():
        raise FileNotFoundError(str(db_path))

    os.unlink(db_path)

    print("Cleanup DONE")


if __name__ == "__main__":
    main()
