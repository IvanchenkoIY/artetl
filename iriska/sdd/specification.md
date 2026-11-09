# Добавить remaining_balance для расчёта остатка оплаты горного тура

Добавить remaining_balance(group, days) в src/quote.py: остаток = quote(group, days) - deposit(group, days), результат int. Сохранить DEPOSIT_PERCENT, комментарий IDE_HANDOFF_V1 и реализацию deposit. Валидация наследуется через вызов quote и deposit. Создать tests/test_balance.py с классом Balance и методами test_regular, test_invalid, test_large. Импорт: from src.quote import quote, deposit, remaining_balance. Старые 7 тестов не менять. Допустимые файлы: src/quote.py, tests/test_balance.py. Без зависимостей.

## Требования

- **REQ-001**: remaining_balance(group, days) возвращает quote(group, days) - deposit(group, days) как int
  Проверка: review 
- **REQ-002**: remaining_balance(1,1)==700 и remaining_balance(5,2)==6300; deposit+remaining_balance==quote
  Проверка: review 
- **REQ-003**: remaining_balance вызывает ValueError при bool, нуле или отрицательных group/days
  Проверка: review 
- **REQ-004**: remaining_balance(10**20,3)==10**20*1890 и тип int
  Проверка: review 
- **REQ-005**: Существующие 7 тестов продолжают проходить без изменений
  Проверка: test test_deposit.Deposit.test_invalid, test_deposit.Deposit.test_large, test_deposit.Deposit.test_regular, test_existing.Existing.test_regular, test_quote_new.QuoteNew.test_discount, test_quote_new.QuoteNew.test_invalid, test_quote_precision.QuotePrecision.test_large

## Вне scope

- Изменение quote
- Изменение deposit
- Изменение существующих тестов
- Добавление зависимостей
- Изменение других файлов

Версия: 2
SHA-256: 14082aa6ac385f407612d3c08b6d1afa795767734e8764064368aa19176caa9b
