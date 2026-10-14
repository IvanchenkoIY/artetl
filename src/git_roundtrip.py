def greet(name: str) -> str:
    """Return a greeting using a trimmed name."""
    return f"Hello, {name.strip() or 'world'}!"
