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


_LABELS = {"hike": "Поход", "cabin": "Домик", "quad": "Квадротур"}


def render_booking(kind, success=False):
    if kind not in KINDS:
        kind = "hike"
    options = "".join(
        f'<option value="{k}"{" selected" if k == kind else ""}>{_LABELS[k]}</option>'
        for k in KINDS
    )
    success_html = '<p>Заявка принята</p>' if success else ""
    style = (
        'style="box-sizing:border-box;max-width:100%;display:block;'
        'font-family:system-ui,sans-serif;margin:0 0 8px;padding:0"'
    )
    btn_style = (
        'style="box-sizing:border-box;max-width:100%;display:block;'
        'background:#2e7d32;color:#fff;border:none;padding:10px;'
        'font-size:1rem;cursor:pointer;margin-top:4px"'
    )
    return (
        f'<form method="post" action="/booking" '
        f'style="box-sizing:border-box;max-width:100%;display:block;'
        f'font-family:system-ui,sans-serif">'
        f'<p style="margin:0 0 12px;font-size:0.9rem;color:#555">'
        f'Демонстрационная заявка: сохраняется локально, организатору не отправляется</p>'
        f'<label for="kind" {style}>Услуга</label>'
        f'<select name="kind" id="kind" {style}>{options}</select>'
        f'<label for="name" {style}>Имя</label>'
        f'<input type="text" name="name" id="name" required maxlength="80" {style}>'
        f'<label for="email" {style}>Email</label>'
        f'<input type="email" name="email" id="email" required maxlength="254" {style}>'
        f'<label for="start_date" {style}>Дата</label>'
        f'<input type="date" name="start_date" id="start_date" required {style}>'
        f'<label for="people" {style}>Человек</label>'
        f'<input type="number" name="people" id="people" min="1" max="12" value="2" required {style}>'
        f'<button type="submit" {btn_style}>Отправить</button>'
        f"{success_html}"
        f"</form>"
    )
