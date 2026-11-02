from db import get_connection, initialize_database

SAMPLE_PRODUCTS = [
    (
        "Wireless Headphones",
        "Comfortable wireless over-ear headphones for music and calls.",
        2499.00,
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800",
        "Electronics",
    ),
    (
        "Smart Watch",
        "A lightweight smartwatch for everyday activity tracking.",
        3999.00,
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800",
        "Electronics",
    ),
    (
        "Running Shoes",
        "Breathable running shoes designed for daily training.",
        1899.00,
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",
        "Fashion",
    ),
    (
        "Travel Backpack",
        "A practical backpack with storage for daily use and travel.",
        1499.00,
        "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800",
        "Accessories",
    ),
    (
        "Desk Lamp",
        "A compact desk lamp suitable for a study or work desk.",
        899.00,
        "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800",
        "Home",
    ),
    (
        "Coffee Mug",
        "A reusable ceramic mug for tea, coffee and other drinks.",
        299.00,
        "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=800",
        "Home",
    ),
]


def seed_database():
    initialize_database()

    with get_connection() as connection:
        count = connection.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        if count == 0:
            connection.executemany(
                """
                INSERT INTO products
                    (name, description, price, image_url, category)
                VALUES (?, ?, ?, ?, ?)
                """,
                SAMPLE_PRODUCTS,
            )
            print(f"Inserted {len(SAMPLE_PRODUCTS)} sample products.")
        else:
            print(f"Database already contains {count} products; seed skipped.")


if __name__ == "__main__":
    seed_database()
