def quote(group, days):
    if isinstance(group, bool) or isinstance(days, bool):
        raise ValueError("group and days must be int, not bool")
    if not isinstance(group, int) or not isinstance(days, int):
        raise ValueError("group and days must be int")
    if group <= 0 or days <= 0:
        raise ValueError("group and days must be positive")
    price = group * days * 1000
    if group >= 5:
        price = int(price * 0.9)
    return price
