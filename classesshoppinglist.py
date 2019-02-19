class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items_to_buy = []
    def __repr__(self):
        return self.name
    def total_amount(self, a, b):
        total = 0
        total += (a*b)
        return total

class ItemChoice:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    def __repr__(self):
        return self.item
    
