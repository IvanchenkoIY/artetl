# Форма заявки и валидация Booking.register

Реализация формы демонстрационной заявки и валидации на стороне сервера. Изменяются только web/signup.html и src/Booking.java. Форма отправляет POST на /signup. Booking.register валидирует name (1-100 символов после trim), email (содержит @ и точку в домене, до 254 символов) и route (только konzhak, taganay, iremel). При успехе возвращает копию валидных полей, при ошибке бросает IllegalArgumentException. В HTML обязательно наличие lang="ru", семантических тегов <nav> и <main>, видимого текста «Демонстрационная заявка». Внешняя визуальная проверка не входит в scope текущей подзадачи.

## Требования

- **REQ-001**: Форма в web/signup.html должна иметь атрибуты method="post" и action="/signup".
  Проверка: test command-1
- **REQ-002**: Форма должна содержать поле name="name" с атрибутом required и связанным label.
  Проверка: test command-1
- **REQ-003**: Форма должна содержать поле name="email" с атрибутом required и связанным label.
  Проверка: test command-1
- **REQ-004**: Форма должна содержать select name="route" с опциями konzhak, taganay, iremel.
  Проверка: test command-1
- **REQ-005**: Страница /signup должна содержать видимый текст «Демонстрационная заявка».
  Проверка: test command-1
- **REQ-006**: Страница /signup должна иметь атрибут lang="ru" в теге html.
  Проверка: test command-1
- **REQ-007**: Страница /signup должна содержать семантические теги <nav> и <main>.
  Проверка: test command-1
- **REQ-008**: Booking.register должен возвращать копию валидных полей name, email, route при корректных данных.
  Проверка: test command-1
- **REQ-009**: Booking.register должен бросать IllegalArgumentException, если name пустой или превышает 100 символов после trim.
  Проверка: test command-1
- **REQ-010**: Booking.register должен бросать IllegalArgumentException, если email не содержит @ или точку в доменной части, либо превышает 254 символа.
  Проверка: test command-1
- **REQ-011**: Booking.register должен бросать IllegalArgumentException, если route не является одним из значений konzhak, taganay, iremel.
  Проверка: test command-1

## Вне scope

- Изменение src/Server.java
- Изменение tests/Check.java
- Реализация реальной оплаты или бронирования
- Добавление внешних зависимостей или CDN
- Изменение других HTML-страниц (index, routes, trail, about)
- Изменение web/style.css

Версия: 1
SHA-256: 732d1d529fd28d7189271c6851d9887ee0ff0b87807be2dc5a62279a7cee0a7c
