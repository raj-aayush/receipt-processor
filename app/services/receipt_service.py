import math
from typing import List

from app.schemas.receipt import Receipt, Item
from app.db import mock_db


def process_retailer(retailer: str) -> int:
    points = 0
    # 1 point per alphanum char in retailer name
    for ch in retailer:
        if ch.isalnum():
            points += 1
    return points


def process_total(total: str) -> int:
    points = 0
    cents = total.split(".")[0]
    cents = int(cents) if cents != "" else 0
    # 50 points if total is round
    if cents == 0:
        points += 50
    # 25 points if the total is a multiple of 0.25
    if cents in [0, 25, 50, 75]:
        points += 25
    return points


def process_purchase_time(time: str) -> int:
    points = 0
    # 10 points if purchase is after 2:00 PM and before 4:00 PM
    [hours, mins] = time.split(":")
    hours = int(hours)
    mins = int(mins)
    if (hours == 14 and mins > 0) or hours == 15:
        points += 10
    return points


def process_purchase_date(date: str) -> int:
    points = 0
    # 6 points if the day is odd number
    day = int(date.split("-")[2])
    if day % 2 == 1:
        points += 6
    return points


def process_items(items: List[Item]) -> int:
    points = 0
    # 5 points for every two items on receipt
    points += len(items)//2
    # If the trimmed len of item desc is a multiple of 3, multiply the
    #    price by 0.2 and round up to the nearest integer. Add points
    for item in items:
        if len(item.shortDescription)%3 == 0:
            points += math.ceil(len(item.shortDescription)*0.2)
    return points


def calculate_receipt_points(receipt: Receipt) -> int:
    points = 0
    points += process_retailer(receipt.retailer)
    points += process_total(receipt.total)
    points += process_purchase_time(receipt.purchaseTime)
    points += process_purchase_date(receipt.purchaseDate)
    points += process_items(receipt.items)
    return mock_db.insert(points)