import pytest

from app.rules.total_cents_multiple_0_25 import total_cents_multiple_0_25


def test_total_cents_multiple_0_25_returns_int():
    result = total_cents_multiple_0_25("65.00")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "total, expected_points",
    [
        ("24.99", 0),  # Not a multiple of 0.25
        ("25.00", 25),  # Is a multiple of 0.25
        ("25.25", 25),  # Is a multiple of 0.25
        ("25.50", 25),  # Is a different multiple of 0.25
    ]
)
def test_total_cents_multiple_0_25_various_cases(total, expected_points):
    assert total_cents_multiple_0_25(total) == expected_points