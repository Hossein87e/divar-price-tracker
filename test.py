from scrape_divar import scrape_price
from database_manager import DatabaseManager
from price import Price
from datetime import datetime

db = DatabaseManager("data/prices.db")

product_id = 1
product_url = "https://torob.com/browse/175/موبایل-و-کالای-دیجیتال/" 

amount = scrape_price(product_url)

if amount is None:
    print("price notfound")
else:
    price_obj = Price(
        price_id=None,
        product_id=product_id,
        amount=amount,
        time=datetime.now().isoformat()
    )

    db.add_price(price_obj)
    print("Saved price:", amount)
