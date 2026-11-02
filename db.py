import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_PATH = INSTANCE_DIR / "ecommerce.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def get_connection():
    """Open a SQLite connection and return rows with named columns."""
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    """Create database tables using schema.sql."""
    schema = SCHEMA_PATH.read_text(encoding="utf-8")
    with get_connection() as connection:
        connection.executescript(schema)


def get_product_by_id(product_id):
    """Return one product as a dictionary, or None if it does not exist."""
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT id, name, description, price, image_url, category, created_at
            FROM products
            WHERE id = ?
            """,
            (product_id,),
        ).fetchone()

    return dict(row) if row else None
