import pytest

from app.schemas.receipt import Item
from app.services.receipt_service import calculate_points,  process_receipt, get_points
from app.db import mock_db


def test_calculate_points_returns_int(make_receipt):
    result = calculate_points(make_receipt())
    assert isinstance(result, int)


@pytest.mark.parametrize(
    "overrides, expected_points",
    [
        ({}, 0),  # default
        ({"retailer": "Target"}, 6),
        ({"total": "100"}, 75),
        ({"items": [
            Item(shortDescription="item1", price="1.00"),
            Item(shortDescription="item2", price="1.00"),
            Item(shortDescription="item3", price="1.00"),
            Item(shortDescription="item4", price="1.00"),
        ]}, 10),
        ({"items": [
            Item(shortDescription="ite", price="10.00")
        ]}, 2),
    ]
)


def test_calculate_points_with_overrides(make_receipt, overrides, expected_points):
    receipt = make_receipt(**overrides)
    assert calculate_points(receipt) == expected_points


def test_process_receipt_inserts_into_db(make_receipt):
    receipt = make_receipt()
    receipt_id = process_receipt(receipt)
    assert receipt_id == 0
    assert mock_db.exists(receipt_id) is True
    assert mock_db.get(receipt_id) == 0
    assert mock_db.get(receipt_id) == calculate_points(receipt)


def test_get_points_returns_int():
    assert isinstance(get_points(0), int)


def test_get_points_raises_exception_when_receipt_not_found():
    with pytest.raises(KeyError):
        get_points(99999)
