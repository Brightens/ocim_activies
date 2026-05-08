class car_class():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} - ₱{self.price}"

    def apply_discount(self, discount_percent: float):
        discounted_price = self.price * (1 - discount_percent / 100)
        return discounted_price