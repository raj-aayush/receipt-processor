# Assumption: purchaseTime is always presented in the following format
# HH:MM where HH is 24 hour time
# 12-hour format is not supported at this time

# 10 points if purchase is after 2:00 PM and before 4:00 PM
def purchase_after_2pm_before_4pm(time: str) -> int:
    [hours, mins] = time.split(":")
    hours = int(hours)
    mins = int(mins)
    return 10 if (hours == 14 and mins > 0) or hours == 15 else 0
