def render_page(success=False):
    """Return a complete Russian HTML page for Konzhakovsky Kamen."""
    success_msg = '<p class="success">Заявка принята</p>' if success else ''
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Конжаковский Камень</title>
<style>
:root {{ --bg: #f0f4e8; --card: #ffffff; --text: #2c3e2d; --accent: #4a7c59; --muted: #6b8f71; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding: 1rem; }}
main {{ max-width: 720px; margin: 0 auto; }}
h1 {{ color: var(--accent); margin-bottom: 1rem; font-size: 1.8rem; }}
section {{ background: var(--card); border-radius: 8px; padding: 1.25rem; margin-bottom: 1rem; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
section h2 {{ color: var(--muted); font-size: 1.1rem; margin-bottom: .5rem; }}
a {{ color: var(--accent); }}
.success {{ color: var(--accent); font-weight: 600; }}
label {{ display: block; margin-bottom: .25rem; font-weight: 500; }}
input {{ width: 100%; padding: .5rem; margin-bottom: .75rem; border: 1px solid var(--muted); border-radius: 4px; }}
button {{ background: var(--accent); color: #fff; border: none; padding: .6rem 1.2rem; border-radius: 4px; cursor: pointer; font-size: 1rem; }}
.note {{ font-size: .85rem; color: var(--muted); margin-top: .5rem; }}
@media (min-width: 600px) {{ body {{ padding: 2rem; }} h1 {{ font-size: 2.2rem; }} }}
</style>
</head>
<body>
<main>
<h1>Конжаковский Камень</h1>
<p><a href="#register">Записаться на прогулку</a></p>
{success_msg}
<section>
<h2>О походе</h2>
<p>Конжаковский Камень — гора на Урале, известная горными панорамами и интересом к прогулкам. Точные маршрут, дату, условия и подготовку нужно согласовать с организатором перед реальным походом.</p>
</section>
<section id="register">
<h2>Запись</h2>
<form method="post" action="/register">
<label for="name">Имя</label>
<input type="text" id="name" name="name" maxlength="80" required>
<label for="email">Email</label>
<input type="email" id="email" name="email" maxlength="254" required>
<button type="submit">Записаться</button>
<p class="note">Учебный сайт: Демонстрационный сайт: заявки сохраняются локально и не передаются организатору.</p>
</form>
</section>
</main>
</body>
</html>"""
