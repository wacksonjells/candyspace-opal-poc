from pathlib import Path
import sqlite3
import zipfile

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
ARCHIVE_PATH = DATA_DIR / "data.zip"
DB_PATH = DATA_DIR / "opal.db"


def extract_archive():
    if not ARCHIVE_PATH.exists():
        raise FileNotFoundError(f"Archive not found: {ARCHIVE_PATH}")

    with zipfile.ZipFile(ARCHIVE_PATH, "r") as archive:
        archive.extractall(DATA_DIR)

    print(f"Extracted {ARCHIVE_PATH.name} -> {DATA_DIR}")


def build_database():
    if DB_PATH.exists():
        DB_PATH.unlink()

    with sqlite3.connect(DB_PATH) as conn:
        for csv_file in DATA_DIR.glob("*.csv"):
            table_name = csv_file.stem

            df = pd.read_csv(csv_file)

            df.to_sql(
                table_name,
                conn,
                if_exists="replace",
                index=False
            )

            print(
                f"Loaded {csv_file.name} -> "
                f"{table_name} ({len(df)} rows)"
            )

    print(f"Created {DB_PATH}")


def main():
    extract_archive()
    build_database()


if __name__ == "__main__":
    main()