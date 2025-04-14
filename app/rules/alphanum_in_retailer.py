# 1 point per alphanum char in retailer name
def alphanum_chars_in_retailer(retailer: str) -> int:
    points = 0
    for ch in retailer:
        if ch.isalnum():
            points += 1
    return points