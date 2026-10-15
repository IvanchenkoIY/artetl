def render_page(success=False):
    """Return a complete Russian HTML page for Konzhakovsky Kamen."""
    css = """
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:Georgia,serif;background:#f0f4e8;color:#2d3a2e;line-height:1.6;padding:1rem}
    .wrap{max-width:720px;margin:0 auto}
    h1{color:#3a5a40;font-size:1.8rem;margin-bottom:.5rem}
    p{margin-bottom:1rem}
    a{color:#588157;text-decoration:underline}
    .form-link{display:inline-block;margin-top:.5rem;padding:.6rem 1.2rem;background:#588157;color:#fff;text-decoration:none;border-radius:4px}
    .form-link:hover{background:#3a5a40}
    form{margin-top:1rem}
    label{display:block;margin-bottom:.3rem;font-weight:bold}
    input{width:100%;padding:.5rem;margin-bottom:1rem;border:1px solid #588157;border-radius:4px}
    button{padding:.6rem 1.2rem;background:#588157;color:#fff;border:none;border-radius:4px;cursor:pointer}
    button:hover{background:#3a5a40}
    .note{font-size:.85rem;color:#555;margin-top:.5rem}
    .success{background:#d4edda;color:#155724;padding:.8rem;border-radius:4px;margin-top:1rem}
    """
    success_msg = '<div class="success">Заявка принята</div>' if success else ""
    return (
        "<!doctype html>"
        '<html lang="ru">'
        "<head>"
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Конжаковский Камень</title>"
        f"<style>{css}</style>"
        "</head>"
        "<body>"
        '<div class="wrap">'
        "<h1>Конжаковский Камень</h1>"
        "<p>Конжаковский Камень — популярный горный хребет в Среднем Урале. "
        "Поход на вершину занимает один день и подходит для начинающих туристов. "
        "Маршрут проходит через лесные тропы и альпийские луга, открывая панорамные виды.</p>"
        "<p>Подготовка: удобная обувь, вода, лёгкая еда, тёплая одежда. "
        "Рекомендуется проверить прогноз погоды и взять с собой аптечку. "
        "Группа не должна превышать 8 человек.</p>"
        '<a class="form-link" href="#form">Записаться на поход</a>'
        f"{success_msg}"
        '<form id="form" method="post" action="/register">'
        "<label for=\"name\">Имя</label>"
        '<input id="name" name="name" type="text" maxlength="80" required>'
        "<label for=\"email\">Email</label>"
        '<input id="email" name="email" type="email" maxlength="254" required>'
        '<button type="submit">Записаться</button>'
        '<p class="note">Учебный сайт: заявки никуда не отправляются.</p>'
        "</form>"
        "</div>"
        "</body>"
        "</html>"
    )
