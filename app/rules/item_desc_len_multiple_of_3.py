import math

# Assumption: Rule specifies multiple of 3
# Zero is a multiple of 3 so an empty string would still trigger this rule


# If the trimmed len of item desc is a multiple of 3, multiply the
#    price by 0.2 and round up to the nearest integer. Add points
def item_desc_len_multiple_of_3(desc: str, price: str) -> int:
    if len(desc.strip()) % 3 == 0:
        return math.ceil(float(price) * 0.2)
    return 0
