# Усиление валидации заявки и приведение формы к ограничениям

Усиление валидации заявки в src/Booking.java и приведение формы web/signup.html к тем же ограничениям. Текущий тест command-1 падает с ошибкой 'unsafe name', что подтверждает необходимость реализации проверки имени. Валидная заявка (Анна/anna@example.org/konzhak) должна сохраняться. Ограничения: только два файла, стандартная библиотека Java, без внешних зависимостей.

## Требования

- **REQ-001**: Имя после trim должно быть длиной от 1 до 100 символов; иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-002**: Имя не должно содержать символы '<', '>' и управляющие символы (включая перевод строки); иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-003**: Email не должен превышать 254 символа; иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-004**: Email должен содержать символ '@' и точку в доменной части; иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-005**: Email не должен содержать пробельные или управляющие символы; иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-006**: Route должен быть одним из: konzhak, taganay, iremel; иначе IllegalArgumentException
  Проверка: test command-1
- **REQ-007**: Валидная заявка (Анна/anna@example.org/konzhak) должна успешно сохраняться
  Проверка: test command-1
- **REQ-008**: Форма /signup должна иметь атрибуты maxlength, соответствующие ограничениям валидации
  Проверка: test command-1
- **REQ-009**: Форма /signup должна содержать подписи полей и подсказку о демонстрационном характере заявки
  Проверка: test command-1
- **REQ-010**: HTML-страница /signup должна иметь lang="ru" в двойных кавычках, семантические <nav> и <main>
  Проверка: test command-1

## Вне scope

- Изменение src/Server.java
- Изменение tests/Check.java
- Изменение других HTML-страниц (index, routes, trail, about)
- Изменение web/style.css
- Добавление новых зависимостей или внешних сервисов

Версия: 1
SHA-256: 03a01d0315d6411ee033726274d098f3457e820afc411103f2ce8b030c493a49
