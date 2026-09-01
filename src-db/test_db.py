import json
import sqlite3
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "opal.db"

TABLES = [
    "customers",
    "campaigns",
    "events",
    "products",
    "transactions",
]

# limit=99999999 is a horrible hack to return everything if not supplied.
def get_data(table, limit=99999999) -> list[dict]:
    conn = sqlite3.connect(
        f"file:{DB_PATH}?mode=ro",
        uri=True
    )
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.execute(
            f"SELECT * FROM {table} LIMIT ?",
            (limit,)
        )

        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()


# python query_db.py : returns all tables
# python query_db.py --table <NAME>
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--table",
        choices=TABLES,
        help="Optional table to query"
    )

    args = parser.parse_args()

    if args.table:
        result = {
            args.table: get_data(args.table, limit=100)
        }
    else:
        result = {
            table: get_data(table, limit=100)
            for table in TABLES
        }

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()