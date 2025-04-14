from typing import List

from app.schemas.receipt import Item

# 5 points for every two items on receipt
def point_every_two_items(items: List[Item]) -> int:
    return len(items)//2 * 5