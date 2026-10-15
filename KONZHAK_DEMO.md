# Демонстрационный сайт «Конжак»

Каждая новая задача продолжает опубликованную ветку предыдущей.
1. Исправить работающую ссылку на форму.
2. Общее оформление и маршруты пяти страниц.
3. Домики: описание и выбор заявки.
4. Квадротуры и обзорные точки: иллюстрации, описания.
5. Общая заявка на поход, домик или тур; проверка и сохранение в SQLite.
Это демонстрационные предложения без оплаты и обещания реальной доступности.
tests/test_site_contract.py — независимый защищённый контракт приёмки.

## Итерация 2
app.py делегирует прежнему Handler в src/server.py (поведение не изменено).
Доработать src/server.py и новый src/site.py: GET / и /cabins, общая навигация,
ровно три JPEG из src/assets по белому списку. На главной сохранить render_page.
GET /assets/credits.json и любой иной путь возвращает 404. /register сохраняется.
Изображения — иллюстрации из открытых источников, авторы/лицензии в PHOTO_CREDITS.md.
Указывать их подписи и ссылки на источник/лицензию прямо на соответствующей странице.

# Фотографии

Иллюстрации, не обещание реального вида услуги. Изображения без изменений.

- mountain.jpg: Makarenko Sasha; CC BY-SA 3.0; https://commons.wikimedia.org/wiki/File:G._Karpinsk,_Sverdlovskaya_oblast%27,_Russia_-_panoramio_(1).jpg; https://creativecommons.org/licenses/by-sa/3.0/
- cabin.jpg: Brian M. Powell; CC BY-SA 3.0; https://commons.wikimedia.org/wiki/File:Monongahela_National_Forest_-_Middle_Mountain_Cabins.jpg; https://creativecommons.org/licenses/by-sa/3.0/
- quad.jpg: Kenneth Allen; CC BY-SA 2.0; https://commons.wikimedia.org/wiki/File:Quad_bike,_Edergole_Road_-_geograph.org.uk_-_1727910.jpg; https://creativecommons.org/licenses/by-sa/2.0/
