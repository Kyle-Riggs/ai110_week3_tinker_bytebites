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

    def is_verified(self) -> bool:
        """A customer is verified if they have at least one past purchase."""
        return len(self.past_purchases) > 0


class FoodItem:
    def __init__(self, name: str, price: Decimal, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items: list[FoodItem] = []

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the items whose category matches exactly."""
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self) -> list[FoodItem]:
        """Return a new list of items, most popular first."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, items: list[FoodItem] | None = None):
        self.items: list[FoodItem] = items if items is not None else []

    def calculate_total(self) -> Decimal:
        """Return the sum of the item prices (0 when there are no items)."""
        return sum((item.price for item in self.items), Decimal("0"))
