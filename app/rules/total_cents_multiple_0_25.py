from .utils import get_cents


# 25 points if the total is a multiple of 0.25
def total_cents_multiple_0_25(total: str) -> int:
    return 25 if get_cents(total) in [0, 25, 50, 75] else 0
