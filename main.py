import math
from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
"""
TODO:
- Dockerize app
- [Simple dict in mem takes care of this req] Setup in mem db
- [See above] Store receipt w point & gen ID (& retrieve receipt)
- Add unit tests for all cases
"""

db = {}

class Item(BaseModel):
    shortDescription: str
    price: str


class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[Item]
    total: str


# Returns a value from 0 to 99
def get_cents(price: str) -> int:
    cents = price.split(".")[0]
    if cents == "":
        return 0
    return int(cents)


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    # 1 point per alphanum char in retailer name
    points = 0
    for ch in receipt.retailer:
        if ch.isalnum():
            points += 1
    # 50 points if total is round
    if get_cents(receipt.total) == 0:
        points += 50
    # 25 points if the total is a multiple of 0.25
    if get_cents(receipt.total) in [0, 25, 50, 75]:
        points += 25
    # 5 points for every two items on receipt
    points += len(receipt.items)//2
    # 10 points if purchase is after 2:00 PM and before 4:00 PM
    [hours, mins] = receipt.purchaseTime.split(":")
    hours = int(hours)
    mins = int(mins)
    if (hours == 14 and mins > 0) or hours == 15:
        points += 10
    # 6 points if the day is odd number
    day = int(receipt.purchaseDate.split("-")[2])
    if day % 2 == 1:
        points += 6
    # If the trimmed len of item desc is a multiple of 3, multiply the
    #    price by 0.2 and round up to the nearest integer. Add points
    for item in receipt.items:
        if len(item.shortDescription)%3 == 0:
            points += math.ceil(len(item.shortDescription)*0.2)
    db[len(db)] = points
    return {"Points": points}


@app.get("/receipt")
def read_item():
    print(db)
    return {}