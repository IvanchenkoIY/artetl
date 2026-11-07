def booking_price(guests, nights):
    return guests * nights * 1000


def tour_duration(kind):
    if kind == 'short':
        return 60
    elif kind == 'long':
        return 180
    else:
        raise ValueError(f"Unknown tour kind: {kind}")
