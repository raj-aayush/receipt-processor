import pytest

from app.schemas.receipt import Item
from app.services.receipt_service import calculate_points


def test_calculate_points_returns_int(default_receipt):
    result = calculate_points(default_receipt)
    assert isinstance(result, int)


def test_calculate_points_returns_zero_when_default_receipt(default_receipt):
    result = calculate_points(default_receipt)
    assert result == 0


def test_calculate_points_returns_six_when_retailer_is_target(default_receipt):
    default_receipt.retailer = "Target"
    result = calculate_points(default_receipt)
    assert result == 6


def test_calculate_points_returns_75_when_total_is_100(default_receipt):
    default_receipt.total = "100"
    result = calculate_points(default_receipt)
    assert result == 75


def test_calculate_points_returns_2_when_4_items(default_receipt):
    default_receipt.items = [
        Item(shortDescription="item1", price="1.00"),
        Item(shortDescription="item2", price="1.00"),
        Item(shortDescription="item3", price="1.00"),
        Item(shortDescription="item4", price="1.00"),
    ]
    result = calculate_points(default_receipt)
    assert result == 10


def test_calculate_points_returns_2(default_receipt):
    default_receipt.items = [
        Item(shortDescription="ite", price="10.00"),
    ]
    result = calculate_points(default_receipt)
    assert result == 2
