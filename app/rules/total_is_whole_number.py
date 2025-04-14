from utils import get_cents

# 50 points if total is round
def total_is_whole_number(total: str) -> int:
    return 50 if get_cents(total) == 0 else 0