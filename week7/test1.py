class GroceryItem:
    name = ""
    weight = 0
    price = 0.0

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def get_price_per_kg(self):
        return (self.price / self.weight) * 1000


banana = GroceryItem("banana", 120, 0.20)
print("Bananas are", banana.get_price_per_kg(), "pounds per kilogram")
