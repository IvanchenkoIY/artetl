# Java: добавление PaymentSummary

Добавление зависимого компонента PaymentSummary и его тестов поверх уже реализованных BookingQuote и QuoteFormatter. Существующие 12 тестов сохраняются. Новые тесты до реализации проверяются вручную (review). Предположение: формат строки строго соответствует спецификации задачи, без дополнительных пробелов или символов.

## Требования

- **REQ-001**: PaymentSummary: public final class, public static String format(BookingQuote quote, long paid). Если quote == null, paid < 0 или paid > quote.total(), выброси IllegalArgumentException. Иначе верни QuoteFormatter.format(quote) + "; paid=" + paid + "; due=" + (quote.total() - paid). Не копируй форматирование QuoteFormatter и формулы DepositPolicy. Целочисленные long, никаких зависимостей/сети.
  Проверка: review 
- **REQ-002**: PaymentSummaryTest: testRegular — BookingQuote.create(5,2) и paid=2700 дают ровно "total=9000; deposit=2700; remaining=6300; paid=2700; due=6300"; paid=0 → due=9000; paid=9000 → due=0.
  Проверка: review 
- **REQ-003**: PaymentSummaryTest: testInvalid — null, paid=-1 и paid=9001 для того же quote должны бросать IllegalArgumentException.
  Проверка: review 
- **REQ-004**: PaymentSummaryTest: testLarge — BookingQuote.create(1000000,3), paid=810000000 дают ровно "total=2700000000; deposit=810000000; remaining=1890000000; paid=810000000; due=1890000000".
  Проверка: review 
- **REQ-005**: Существующие 12 тестов продолжают проходить без изменений.
  Проверка: test BookingQuoteTest#testInvalid, BookingQuoteTest#testLarge, BookingQuoteTest#testRegular, DepositPolicyTest#testInvalid, DepositPolicyTest#testLarge, DepositPolicyTest#testRegular, QuoteFormatterTest#testInvalid, QuoteFormatterTest#testLarge, QuoteFormatterTest#testRegular, TourPriceTest#testInvalid, TourPriceTest#testLarge, TourPriceTest#testRegular

## Вне scope

- Изменение TourPrice.java, DepositPolicy.java, BookingQuote.java, QuoteFormatter.java
- Изменение tests/Check.java и существующих тестов
- Добавление зависимостей, фреймворков, сетевых вызовов
- Миграции БД, API, UI
- Слияние в основную ветку

Версия: 2
SHA-256: 6053af42c57e8d315289bb69ed534aba1e270777b7f007bc2a47c49d9ed43197
