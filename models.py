# ByteBites backend models
#
# Customer:    a ByteBites user, with a name and a history of past purchases
#              (Transactions) that can be used to verify they are a real user.
# FoodItem:    a single item for sale, with a name, price, category and
#              popularity rating.
# Menu:        the full collection of FoodItems; can filter them by category
#              (e.g. "Drinks" or "Desserts").
# Transaction: a group of selected FoodItems that makes up one purchase;
#              computes the total cost.
