#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - (self.total - self.items[-1])
            self.total -= last_item_price
            self.items.pop()

# Example usage:
register = CashRegister(discount=10)
register.add_item("Item 1", 5.99, 2)
register.add_item("Item 2", 9.99)
register.apply_discount()
print(f"Total: ${register.total:.2f}")
register.void_last_transaction()
print(f"Total after voiding last transaction: ${register.total:.2f}")

