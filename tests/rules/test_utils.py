import pytest

from app.rules.utils import get_cents


@pytest.mark.parametrize(
    "total, expected_cents",
    [
        ("24.99", 99),
        ("25", 0),  # no decimal
        ("25.", 0),  # decimal with no cents
        ("25.0", 0),  # decimal with 1 cent
        ("25.00", 0),  # decimal with 2 cents
        ("25.25", 25),
        ("25.50", 50),
    ]
)
def test_get_cents_various_cases(total, expected_cents):
    assert get_cents(total) == expected_cents
