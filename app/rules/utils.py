def get_cents(price: str) -> int:
    cents = price.split(".")[1] if price.find(".") != -1 else ""
    cents = int(cents) if cents != "" else 0
    return cents