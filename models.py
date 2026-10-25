# ByteBites backend models
#
# Customer:    a ByteBites user, with a name and a history of past purchases
#              (Transactions) that can be used to verify they are a real user.
# FoodItem:    a single item for sale, with a name, price, category and
#              popularity rating.
# Menu:        the full collection of FoodItems; can filter them by category
#              (e.g. "Drinks" or "Desserts") and sort them by popularity.
# Transaction: a group of selected FoodItems that makes up one purchase;
#              computes the total cost.

from decimal import Decimal


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.past_purchases: list["Transaction"] = []


class FoodItem:
    def __init__(self, name: str, price: Decimal, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items: list[FoodItem] = []


class Transaction:
    def __init__(self, items: list[FoodItem] | None = None):
        self.items: list[FoodItem] = items if items is not None else []
