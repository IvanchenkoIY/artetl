import sqlite3
from datetime import date
from html import escape
from src.registration import _validate_name, _validate_email

KINDS = ("hike", "cabin", "quad")


def _validate_kind(kind):
    if kind not in KINDS:
        raise ValueError("kind must be hike, cabin or quad")
    return kind


def _validate_date(value):
    if not isinstance(value, str) or len(value) != 10:
        raise ValueError("start_date must be YYYY-MM-DD")
    y, m, d = value.split("-")
    if not (y.isdigit() and m.isdigit() and d.isdigit()):
        raise ValueError("start_date must be YYYY-MM-DD")
    try:
        parsed = date(int(y), int(m), int(d))
    except ValueError:
        raise ValueError("start_date must be a valid date")
    if parsed.isoformat() != value or parsed < date.today():
        raise ValueError("start_date must be today or later")
    return value


def _validate_people(value):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("people must be an integer")
    if not 1 <= value <= 12:
        raise ValueError("people must be 1..12")
    return value


def submit_booking(db_path, kind, name, email, start_date, people):
    kind = _validate_kind(kind)
    name = _validate_name(name)
    email = _validate_email(email)
    start_date = _validate_date(start_date)
    people = _validate_people(people)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS bookings ("
            "kind TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, "
            "start_date TEXT NOT NULL, people INTEGER NOT NULL)"
        )
        conn.execute(
            "INSERT INTO bookings (kind, name, email, start_date, people) VALUES (?, ?, ?, ?, ?)",
            (kind, name, email, start_date, people),
        )
        conn.commit()
    finally:
        conn.close()
    return None


def render_booking(kind, success=False):
    if kind not in KINDS:
        kind = "hike"
    options = "".join(
        f'<option value="{k}"{" selected" if k == kind else ""}>{k}</option>' for k in KINDS
    )
    success_html = '<p>Заявка принята</p>' if success else ""
    return (
        f'<form method="post" action="/booking">'
        f'<label for="kind">Услуга</label>'
        f'<select name="kind" id="kind">{options}</select>'
        f'<label for="name">Имя</label>'
        f'<input type="text" name="name" id="name" required>'
        f'<label for="email">Email</label>'
        f'<input type="email" name="email" id="email" required>'
        f'<label for="start_date">Дата</label>'
        f'<input type="date" name="start_date" id="start_date" required>'
        f'<label for="people">Человек</label>'
        f'<input type="number" name="people" id="people" min="1" max="12" required>'
        f'<button type="submit">Отправить</button>'
        f"{success_html}"
        f"</form>"
    )
