import pytest

from app.rules.point_every_two_items import point_every_two_items
from app.schemas.receipt import Item


def test_point_every_two_items_returns_int():
    result = point_every_two_items([Item(shortDescription="item1", price="1")])
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "items, expected_points",
    [
        ([], 0),  # No items
        ([
             Item(shortDescription="item1", price="1")
         ], 0),  # One item
        ([
             Item(shortDescription="item1", price="1"),
             Item(shortDescription="item2", price="2")
         ], 5),  # Two items
        ([
             Item(shortDescription="item1", price="1"),
             Item(shortDescription="item2", price="2"),
             Item(shortDescription="item3", price="3")
         ], 5),  # Three items
        ([
             Item(shortDescription="item1", price="1"),
             Item(shortDescription="item2", price="2"),
             Item(shortDescription="item3", price="3"),
             Item(shortDescription="item4", price="4")
         ], 10),  # Four items
    ]
)
def test_point_every_two_items_various_cases(items, expected_points):
    assert point_every_two_items(items) == expected_points