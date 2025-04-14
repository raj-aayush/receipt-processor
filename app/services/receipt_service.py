from app.rules import (
    alphanum_chars_in_retailer,
    total_is_whole_number,
    total_cents_multiple_0_25,
    purchase_after_2pm_before_4pm,
    purchase_date_value_odd,
    point_every_two_items,
    item_desc_len_multiple_of_3,
)
from app.schemas.receipt import Receipt
from app.db import mock_db


def process_receipt(receipt: Receipt) -> int:
    points = calculate_points(receipt)
    return mock_db.insert(points)


def calculate_points(receipt: Receipt) -> int:
    points = 0
    points += alphanum_chars_in_retailer(receipt.retailer)
    points += total_is_whole_number(receipt.total)
    points += total_cents_multiple_0_25(receipt.total)
    points += purchase_after_2pm_before_4pm(receipt.purchaseTime)
    points += purchase_date_value_odd(receipt.purchaseDate)
    points += point_every_two_items(receipt.items)
    for item in receipt.items:
        points += item_desc_len_multiple_of_3(item.shortDescription, item.price)
    return points