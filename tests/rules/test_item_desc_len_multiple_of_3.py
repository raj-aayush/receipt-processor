import pytest
from app.rules import item_desc_len_multiple_of_3
from app.schemas.receipt import Item


def test_item_desc_len_multiple_of_3_returns_int():
    result = item_desc_len_multiple_of_3("123456", "5.00")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "desc, price, expected_total",
    [
        # When length is a multiple of 3
        ("", "5", 1),
        ("123", "5", 1),
        ("123456", "5", 1),
        # When length is not a multiple of 3
        ("So", "5", 0),
        ("1234", "5", 0),
        # When length is multiple of 3, try different prices
        ("123", "0", 0),
        ("123", "2.53", 1),
        ("123", "12.53", 3),
        ("123", "1093.53", 219)
    ]
)
def test_item_desc_len_multiple_of_3_various_cases(desc, price, expected_total):
    assert item_desc_len_multiple_of_3(desc, price) == expected_total