# Добавить функцию deposit для расчёта предоплаты горного тура

Добавить функцию deposit(group, days) в src/quote.py: предоплата 30% от quote(group, days), округлённая вверх до целого рубля. Использовать только целочисленную арифметику: (quote(group, days) * 30 + 99) // 100. Поведение quote не менять, прежние тесты сохранить. Создать новый tests/test_deposit.py с unittest-классом Deposit и методами test_regular, test_invalid, test_large. Импорт в тесте: from quote import deposit. Разрешены только src/quote.py и новый tests/test_deposit.py. Не добавлять зависимости.

## Требования

- **REQ-001**: Функция deposit(group, days) вычисляет предоплату как 30% от quote(group, days), округлённую вверх до целого рубля, используя формулу (quote(group, days) * 30 + 99) // 100
  Проверка: review 
- **REQ-002**: deposit(1, 1) возвращает 300, deposit(5, 2) возвращает 2700
  Проверка: review 
- **REQ-003**: deposit вызывает ValueError при передаче bool, нуля или отрицательного значения в group или days
  Проверка: review 
- **REQ-004**: deposit(10**20, 3) возвращает 10**20 * 810 и тип результата int
  Проверка: review 
- **REQ-005**: Поведение quote не меняется, все исходные тесты проходят
  Проверка: test test_existing.Existing.test_regular, test_quote_new.QuoteNew.test_discount, test_quote_new.QuoteNew.test_invalid, test_quote_precision.QuotePrecision.test_large

## Вне scope

- Изменение поведения quote
- Изменение существующих тестов
- Добавление внешних зависимостей
- Изменение других файлов

Версия: 1
SHA-256: a557c64705d8cecf758f349bc285d6e0d87f0c27d17df9beab135be956fedee6
