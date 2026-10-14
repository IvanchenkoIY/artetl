def greet(name: str) -> str:
    """Return a short greeting; blank names use world."""
    return f"Hi, {name.strip() or 'world'}!"
