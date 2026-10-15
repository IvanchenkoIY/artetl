CSS='<style>body{font-family:system-ui,sans-serif;max-width:720px;margin:auto;padding:1rem;line-height:1.6}nav a{margin-right:1rem}img{max-width:100%;border-radius:6px}figcaption{font-size:.85rem;color:#666;margin-top:.3rem}</style>'

def _page(title, nav, body):
    return ('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>'+title+'</title>'+CSS+'</head><body>'+nav+body+'</body></html>')

def render_quad(nav):
    body=('<h1>Квадротуры</h1><p>Демонстрационный тур на квадроциклах. '
          'Учебный сайт: без оплаты и обещания реальной доступности.</p>'
          '<figure><img src="/assets/quad.jpg" alt="Иллюстрация квадроцикла">'
          '<figcaption>Иллюстрация, не обещание реального вида. Автор: Kenneth Allen, '
          '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA 2.0</a>, '
          '<a href="https://commons.wikimedia.org/wiki/File:Quad_bike,_Edergole_Road_-_geograph.org.uk_-_1727910.jpg">источник</a>.</figcaption></figure>'
          '<p><a href="/#register">Записаться</a></p>')
    return _page('Квадротуры — Конжак', nav, body)

def render_views(nav):
    body=('<h1>Обзорные точки</h1><p>Демонстрационная обзорная прогулка с панорамой Конжака. '
          'Учебный сайт: без оплаты и обещания реальной доступности.</p>'
          '<figure><img src="/assets/mountain.jpg" alt="Панорама горы Конжак">'
          '<figcaption>Иллюстрация, не обещание реального вида. Автор: Makarenko Sasha, '
          '<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, '
          '<a href="https://commons.wikimedia.org/wiki/File:G._Karpinsk,_Sverdlovskaya_oblast%27,_Russia_-_panoramio_(1).jpg">источник</a>.</figcaption></figure>'
          '<p><a href="/#register">Записаться</a></p>')
    return _page('Обзорные точки — Конжак', nav, body)
