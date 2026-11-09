DEPOSIT_PERCENT = 30
# IDE_HANDOFF_V1: keep the human-reviewed integer deposit calculation.


def quote(group, days):
    if isinstance(group, bool) or isinstance(days, bool):
        raise ValueError("group and days must be int, not bool")
    if not isinstance(group, int) or not isinstance(days, int):
        raise ValueError("group and days must be int")
    if group <= 0 or days <= 0:
        raise ValueError("group and days must be positive")
    if group >= 5:
        return group * days * 900
    return group * days * 1000


def deposit(group, days):
    return (quote(group, days) * DEPOSIT_PERCENT + 99) // 100


def remaining_balance(group, days):
    return quote(group, days) - deposit(group, days)
