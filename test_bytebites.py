from decimal import Decimal

import pytest

from models import Customer, FoodItem, Menu, Transaction


@pytest.fixture
def burger():
    return FoodItem("Spicy Burger", Decimal("10.00"), "Mains", 4.5)


@pytest.fixture
def soda():
    return FoodItem("Large Soda", Decimal("5.00"), "Drinks", 4.0)


@pytest.fixture
def cake():
    return FoodItem("Chocolate Cake", Decimal("6.50"), "Desserts", 4.8)


@pytest.fixture
def menu(burger, soda, cake):
    m = Menu()
    m.items.extend([burger, soda, cake])
    return m


# --- Transaction totals ---

def test_calculate_total_with_multiple_items(burger, soda):
    # A $10 burger and a $5 soda cost $15.
    assert Transaction([burger, soda]).calculate_total() == Decimal("15.00")


def test_order_total_is_zero_when_empty():
    # A transaction with nothing added totals $0 instead of crashing.
    assert Transaction().calculate_total() == Decimal("0")


def test_calculate_total_counts_duplicate_items(soda):
    # Picking the same item twice charges for it twice.
    assert Transaction([soda, soda]).calculate_total() == Decimal("10.00")


# --- Menu filtering ---

def test_filter_by_category_returns_only_matching_items(menu, soda):
    # Filtering "Drinks" returns only the drink.
    assert menu.filter_by_category("Drinks") == [soda]


def test_filter_by_category_returns_empty_list_when_no_match(menu):
    # A category with no items gives an empty list.
    assert menu.filter_by_category("Sides") == []


def test_filter_by_category_on_empty_menu():
    # Filtering an empty menu gives an empty list.
    assert Menu().filter_by_category("Drinks") == []


# --- Menu sorting ---

def test_sort_by_popularity_orders_most_popular_first(menu, burger, soda, cake):
    # Highest popularity rating comes first.
    assert menu.sort_by_popularity() == [cake, burger, soda]


def test_sort_by_popularity_does_not_change_menu_order(menu, burger, soda, cake):
    # Sorting returns a new list and leaves the menu's own order alone.
    menu.sort_by_popularity()
    assert menu.items == [burger, soda, cake]


# --- Customer verification ---

def test_customer_without_purchases_is_not_verified():
    # A brand-new customer has no history, so cannot be verified.
    assert Customer("Ada").is_verified() is False


def test_customer_with_past_purchase_is_verified(burger):
    # Having at least one past purchase verifies the customer.
    customer = Customer("Ada")
    customer.past_purchases.append(Transaction([burger]))
    assert customer.is_verified() is True
