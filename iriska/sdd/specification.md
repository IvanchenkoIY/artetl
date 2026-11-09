# Java: расчёт оплаты бронирования

Расчёт предоплаты (30%, округление вверх, long) и представление бронирования. Три последовательные подзадачи: DepositPolicy → BookingQuote → QuoteFormatter. Существующие TourPrice и тесты сохраняются. Новые тесты до реализации проверяются вручную (review).

## Требования

- **REQ-001**: DepositPolicy: public final class, static long deposit(long total) и static long remaining(long total). total <= 0 → IllegalArgumentException. deposit = 30% с округлением вверх: total/100*30 + (total%100*30+99)/100. remaining = total - deposit(total). Без float/double, без переполнения для Long.MAX_VALUE.
  Проверка: review 
- **REQ-002**: DepositPolicyTest: testRegular (1000→300, остаток 700; 1→1, остаток 0), testInvalid (0 и -1 → IllegalArgumentException), testLarge (Long.MAX_VALUE → 2767011611056432743L, сумма с остатком = Long.MAX_VALUE).
  Проверка: review 
- **REQ-003**: BookingQuote: public record BookingQuote(int group, int days, long total, long deposit, long remaining). static BookingQuote create(int group, int days) использует TourPrice.quote и DepositPolicy, не копирует формулу расчёта.
  Проверка: review 
- **REQ-004**: BookingQuoteTest: testRegular (create(5,2): total=9000, deposit=2700, remaining=6300, group=5, days=2), testInvalid (group=0, days=0, отрицательные → IllegalArgumentException), testLarge (create(1000000,3): total=2700000000L, deposit=810000000L, remaining=1890000000L).
  Проверка: review 
- **REQ-005**: QuoteFormatter: public final class, static String format(BookingQuote q). null → IllegalArgumentException. Формат: "total=<total>; deposit=<deposit>; remaining=<remaining>".
  Проверка: review 
- **REQ-006**: QuoteFormatterTest: testRegular (create(1,1) → "total=1000; deposit=300; remaining=700"), testInvalid (null → IllegalArgumentException), testLarge (create(1000000,3) → "total=2700000000; deposit=810000000; remaining=1890000000").
  Проверка: review 
- **REQ-007**: Существующие тесты TourPriceTest продолжают проходить без изменений.
  Проверка: test TourPriceTest#testInvalid, TourPriceTest#testLarge, TourPriceTest#testRegular

## Вне scope

- Изменение TourPrice.java и TourPriceTest.java
- Изменение tests/Check.java
- Добавление зависимостей, фреймворков, сетевых вызовов
- Миграции БД, API, UI
- Слияние в основную ветку

Версия: 1
SHA-256: 6b8ad65be709f2fd6edb1532eb26755f0cea5f03c605b62cd716b802f2df7154
