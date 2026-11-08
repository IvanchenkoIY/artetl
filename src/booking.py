def register(name, email, route):
    """Return validated fields name/email/route, or raise ValueError."""
    if not isinstance(name, str) or not isinstance(email, str) or not isinstance(route, str):
        raise ValueError("Invalid input")
    name = name.strip()
    if len(name) < 1 or len(name) > 100:
        raise ValueError("Invalid name")
    if '<' in name or '>' in name:
        raise ValueError("Invalid name")
    if any(ord(c) < 32 or ord(c) == 127 for c in name):
        raise ValueError("Invalid name")
    email = email.strip()
    if len(email) > 254:
        raise ValueError("Invalid email")
    if any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in email):
        raise ValueError("Invalid email")
    if "@" not in email:
        raise ValueError("Invalid email")
    local, domain = email.rsplit("@", 1)
    if not local or not domain or "." not in domain:
        raise ValueError("Invalid email")
    if route not in ("konzhak", "taganay", "iremel"):
        raise ValueError("Invalid route")
    return {"name": name, "email": email, "route": route}
