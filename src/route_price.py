def discounted_total(prices, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be 0..100")
    return round(sum(prices) * (1 - percent / 100), 2)


def per_person(total, people):
    if people <= 0:
        raise ValueError("people must be > 0")
    return round(total / people, 2)


def deposit_amount(total, percent):
    if total < 0:
        raise ValueError("total must be >= 0")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be 0..100")
    return round(total * percent / 100, 2)


def balance_due(total, paid):
    if total < 0:
        raise ValueError("total must be >= 0")
    if paid < 0 or paid > total:
        raise ValueError("paid must be 0..total")
    return round(total - paid, 2)
