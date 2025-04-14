import pytest

from app.rules.total_is_whole_number import total_is_whole_number


def test_total_is_whole_number_returns_int():
    result = total_is_whole_number("26")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "total, expected_points",
    [
        ("24.99", 0),  # Not a multiple of 0.25 & is not a round dollar amount
        ("25.00", 50),  # Is a round dollar amount
        ("25.25", 0),  # Is not a round dollar amount
        ("25.50", 0),  # Is not a round dollar amount
    ]
)
def test_total_is_whole_number_various_cases(total, expected_points):
    assert total_is_whole_number(total) == expected_points