import pytest
from app.rules import alphanum_chars_in_retailer

def test_alphanum_chars_in_retailer_returns_int():
    result = alphanum_chars_in_retailer("...")
    assert isinstance(result, int)

@pytest.mark.parametrize(
    "retailer, expected_points",
    [
        ("...", 0), # No alpha num chars
        ("target", 6), # All lower case chars
        ("TARGETS", 7), # All upper case chars
        ("1234", 4), # All number chars
        ("TAR#GET#123", 9) # Mix of uppercase, lowercase, numbers & symbols
    ]
)
def test_alphanum_chars_in_retailer_various_cases(retailer, expected_points):
    assert alphanum_chars_in_retailer(retailer) == expected_points
