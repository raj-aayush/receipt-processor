# 6 points if the day is odd number
def purchase_date_value_odd(date: str) -> int:
    day = int(date.split("-")[2])
    return 6 if day % 2 == 1 else 0