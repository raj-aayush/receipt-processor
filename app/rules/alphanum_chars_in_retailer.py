# 1 point per alphanum char in retailer name
def alphanum_chars_in_retailer(retailer: str) -> int:
    return sum(1 for char in retailer if char.isalnum())
