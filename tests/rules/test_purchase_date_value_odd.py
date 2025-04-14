import pytest

from app.rules.purchase_date_value_odd import purchase_date_value_odd


def test_purchase_date_value_odd_returns_int():
    result = purchase_date_value_odd("2024-10-01")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "date, expected_points",
    [
        ("2024-10-01", 6),  # Odd day
        ("2024-10-02", 0),  # Even day
        ("2024-11-02", 6),  # Odd month
        ("2025-10-02", 0),  # Odd year
    ]
)
def test_purchase_date_value_odd_various_cases(date, expected_points):
    assert purchase_date_value_odd(date) == expected_points