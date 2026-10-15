import sqlite3


def _validate_name(name):
    if not isinstance(name, str):
        raise ValueError("name must be a string")
    name = name.strip()
    if len(name) < 2 or len(name) > 80:
        raise ValueError("name must be 2-80 characters after strip")
    return name


def _validate_email(email):
    if not isinstance(email, str):
        raise ValueError("email must be a string")
    email = email.strip()
    if len(email) > 254:
        raise ValueError("email too long")
    if email.count("@") != 1:
        raise ValueError("email must contain exactly one @")
    local, domain = email.split("@")
    if not local or not domain:
        raise ValueError("email local and domain must be non-empty")
    if "." not in domain:
        raise ValueError("email domain must contain a dot")
    for ch in email:
        if ch.isspace() or ord(ch) < 32 or ch == "\x7f":
            raise ValueError("email must not contain whitespace or control characters")
    return email


def register(db_path, name, email):
    """Validate and persist one registration in SQLite; raise ValueError on bad input."""
    name = _validate_name(name)
    email = _validate_email(email)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS registrations (name TEXT NOT NULL, email TEXT NOT NULL)"
        )
        conn.execute("INSERT INTO registrations (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    finally:
        conn.close()
    return None
