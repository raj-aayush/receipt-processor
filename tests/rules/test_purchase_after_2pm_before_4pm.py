import pytest

from app.rules.purchase_after_2pm_before_4pm import purchase_after_2pm_before_4pm


def test_purchase_after_2pm_before_4pm_returns_int():
    result = purchase_after_2pm_before_4pm("14:30")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "time, expected_points",
    [
        ("13:59", 0),  # Before 2 PM
        ("14:00", 0),  # Exactly 2 PM
        ("14:01", 10),  # After 2 PM
        ("15:00", 10),  # Exactly 3 PM
        ("15:59", 10),  # Before 4 PM
        ("16:00", 0),  # Exactly 4 PM
        ("18:00", 0),  # After 4 PM
    ]
)
def test_purchase_after_2pm_before_4pm_various_cases(time, expected_points):
    assert purchase_after_2pm_before_4pm(time) == expected_points