# Assumption: purchaseDate must be in the following format
# YYYY-MM-DD
# Any other date formats are not supported at this time


# 6 points if the day is odd number
def purchase_date_value_odd(date: str) -> int:
    day = int(date.split("-")[2])
    return 6 if day % 2 == 1 else 0
