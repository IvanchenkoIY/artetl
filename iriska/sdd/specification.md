# Целочисленная арифметика в src/quote.py

Устранить потерю точности в src/quote.py: заменить float-арифметику на целочисленную. Контракт quote(group, days) неизменен: int (не bool), >0, иначе ValueError; 1000 руб/чел/день; скидка 10% при group>=5. Результат для любого положительного int (включая 10**20) должен быть точным целым числом. Допустимые файлы: src/quote.py и новый tests/test_quote_precision.py. Существующие тесты не изменяются. Незакрытые допущения: нет — цель и ограничения ясны из objective.

## Требования

- **REQ-001**: Сохранить существующий контракт quote(): int (не bool), >0, иначе ValueError; 1000 руб/чел/день; скидка 10% при group>=5. Все три исходных теста проходят без изменений.
  Проверка: test test_existing.Existing.test_regular, test_quote_new.QuoteNew.test_discount, test_quote_new.QuoteNew.test_invalid
- **REQ-002**: src/quote.py вычисляет цену строго целочисленной арифметикой: без float, без int(price * 0.9). При group>=5 результат равен group*days*900, иначе group*days*1000. Для group=10**20, days=3 результат равен 10**20*3*900 и имеет тип int.
  Проверка: review 
- **REQ-003**: Создан новый файл tests/test_quote_precision.py с unittest-классом QuotePrecision и методом test_large, проверяющим quote(10**20, 3) == 10**20*3*900 и isinstance(result, int).
  Проверка: review 

## Вне scope

- Изменение сигнатуры quote()
- Добавление внешних зависимостей
- Изменение tests/test_existing.py и tests/test_quote_new.py
- Изменение README.md

Версия: 1
SHA-256: 0e3f64afd62dda1a0841897ffd035284186c8a2c5d98612ce4b6829f81612fc3
