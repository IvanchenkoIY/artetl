# Форма заявки и валидация register

Реализация формы заявки и функции register. Допущение: сервер уже обрабатывает POST /signup и вызывает register (судя по импорту в server.py), поэтому задача ограничена только двумя разрешёнными файлами. Текущий тест command-1 падает на проверке наличия <form в /signup.

## Требования

- **REQ-001**: Страница /signup содержит форму с method="post" и action="/signup"
  Проверка: test command-1
- **REQ-002**: Форма содержит поле name="name" с label и required
  Проверка: test command-1
- **REQ-003**: Форма содержит поле name="email" с label и required
  Проверка: test command-1
- **REQ-004**: Форма содержит select name="route" с вариантами konzhak, taganay, iremel
  Проверка: test command-1
- **REQ-005**: Страница /signup содержит видимый текст «Демонстрационная заявка»
  Проверка: test command-1
- **REQ-006**: Функция register возвращает dict с ключами name, email, route при валидных данных
  Проверка: test command-1
- **REQ-007**: Функция register бросает ValueError при невалидном имени (длина вне 1-100 после trim)
  Проверка: test command-1
- **REQ-008**: Функция register бросает ValueError при невалидном email (отсутствие @ или точки в домене, длина > 254)
  Проверка: test command-1
- **REQ-009**: Функция register бросает ValueError при route, не входящем в список [konzhak, taganay, iremel]
  Проверка: test command-1
- **REQ-010**: Страница /signup имеет lang="ru" в двойных кавычках, семантические <nav> и <main>
  Проверка: test command-1

## Вне scope

- Изменение src/server.py
- Изменение tests/check.py
- Добавление внешних зависимостей
- Реализация оплаты или реального бронирования
- Изменение других HTML-страниц

Версия: 1
SHA-256: 1ef2c4eac218b57d2a7150df6266a57164c4aa810eb5a3d5a416828c9985ded0
