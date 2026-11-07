from datetime import datetime


class Product:
    def __init__(self, product_id, user_id, name, url, created_at):
        self.product_id = product_id
        self.user_id = user_id
        self.name = name
        self.url = url
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at

    def is_valid(self):
        if self.name is None:
            return False

        if self.name == "":
            return False

        if self.url is None:
            return False

        if not self.url.startswith("http"):
            return False

        return True

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "user_id": self.user_id,
            "name": self.name,
            "url": self.url,
            "created_at": self.created_at,
        }
    