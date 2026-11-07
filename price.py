from datetime import datetime

class Price:
    def __init__(self, price_id, product_id, amount, time=None):
        self.price_id = price_id
        self.product_id = product_id
        self.amount = amount
        self.time = time or datetime.now().isoformat()

    def is_valid(self):
        return self.amount is not None and self.amount > 0

    def to_dict(self):
        return {
            "price_id": self.price_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "time": self.time,
        }
