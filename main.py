from database_manager import DatabaseManager
from product import Product
from price import Price


def main():
    db = DatabaseManager()

    product = Product(
        product_id=None,
        user_id=101,
        name="Laptop",
        url="http://example.com/laptop",
        created_at=None
    )
    db.add_product(product)

    products = db.get_all_products()
    for prod in products:
        print(prod.to_dict())

    if products:
        first_product = products[0]

        price = Price(
            price_id=None,
            product_id=first_product.product_id,
            amount=1500.0,
            time=None
        )
        db.add_price(price)

        prices = db.get_prices_for_product(first_product.product_id)
        for pr in prices:
            print(pr.to_dict())

if __name__ == "__main__":
    main()
