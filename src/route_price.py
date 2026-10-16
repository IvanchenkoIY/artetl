def discounted_total(prices, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be 0..100")
    return round(sum(prices) * (1 - percent / 100), 2)


def per_person(total, people):
    if people <= 0:
        raise ValueError("people must be > 0")
    return round(total / people, 2)
