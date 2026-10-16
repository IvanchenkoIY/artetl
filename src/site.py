from src.page import render_page
from src.activities import render_quad, render_views, _page
from src.booking import render_booking

NAV='<nav><a href="/">Главная</a> <a href="/cabins">Домики</a> <a href="/quad">Квадротуры</a> <a href="/views">Обзорные</a> <a href="/booking">Заявка</a></nav>'

def render_route(path, success=False, kind=None):
    if path=='/':
        html=render_page(success)
        return html.replace('<main>', '<main>'+NAV, 1)
    if path=='/cabins':
        return ('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Домики — Конжак</title><style>body{font-family:system-ui,sans-serif;max-width:720px;margin:auto;padding:1rem;line-height:1.6}nav a{margin-right:1rem}img{max-width:100%;border-radius:6px}figcaption{font-size:.85rem;color:#666;margin-top:.3rem}</style></head><body>'
        +NAV+'<h1>Домики</h1><p>Демонстрационные варианты размещения. Учебный сайт, без оплаты и обещания реальной доступности.</p>'
        '<section><h2>Домик у горы</h2><p>Уютный домик для 2–4 человек с печкой и видом на хребет.</p>'
        '<figure><img src="/assets/cabin.jpg" alt="Иллюстрация домика"><figcaption>Иллюстрация, не обещание реального вида. Автор: Brian M. Powell, <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/wiki/File:Monongahela_National_Forest_-_Middle_Mountain_Cabins.jpg">источник</a>.</figcaption></figure></section>'
        '<section><h2>Домик в лесу</h2><p>Тихое место среди сосен, подходит для небольших компаний.</p></section>'
        '<p><a href="/booking?kind=cabin">Записаться</a></p></body></html>')
    if path=='/quad':
        return render_quad(NAV).replace('/#register', '/booking?kind=quad')
    if path=='/views':
        return render_views(NAV).replace('/#register', '/booking?kind=hike')
    if path=='/booking':
        return _page('Заявка — Конжак', NAV, render_booking(kind, success))
    return None
