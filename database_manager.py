import sqlite3
from product import Product
from price import Price

DATABASE_PATH = "tracker.db"

class DatabaseManager:
    def __init__(self, db_path=DATABASE_PATH):
        self.path = db_path
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            name TEXT,
            url TEXT,
            time TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            price_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            amount REAL,
            time TEXT
        )
        """)

        self.connection.commit()


    def add_product(self, product: Product):
        self.cursor.execute("""
        INSERT INTO products (product_id, user_id, name, url, time)
        VALUES (?, ?, ?, ?, ?)
        """, (
            product.product_id,
            product.user_id,
            product.name,
            product.url,
            product.created_at
        ))
        self.connection.commit()

    def get_product(self, product_id):
        row = self.cursor.execute(
            "SELECT product_id, user_id, name, url, time FROM products WHERE product_id = ?",
            (product_id,)
        ).fetchone()

        if row:
            return Product(row[0], row[1], row[2], row[3], row[4])
        return None

    def get_all_products(self):
        rows = self.cursor.execute(
            "SELECT product_id, user_id, name, url, time FROM products"
        ).fetchall()

        return [Product(r[0], r[1], r[2], r[3], r[4]) for r in rows]

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE product_id = ?", (product_id,))
        self.connection.commit()

    def add_price(self, price: Price):
        self.cursor.execute("""
        INSERT INTO prices (product_id, amount, time)
        VALUES (?, ?, ?)
        """, (
            price.product_id,
            price.amount,
            price.time
        ))
        self.connection.commit()

    def get_prices_for_product(self, product_id):
        rows = self.cursor.execute(
            """SELECT price_id, product_id, amount, time 
            FROM prices 
            WHERE product_id = ? 
            ORDER BY time ASC
                """,
            (product_id,)
        ).fetchall()

        return [Price(r[0], r[1], r[2], r[3]) for r in rows]

    def delete_price(self, price_id):
        self.cursor.execute("DELETE FROM prices WHERE price_id = ?", (price_id,))
        self.connection.commit()
