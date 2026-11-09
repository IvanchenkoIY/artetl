Implement only the current approved unit in the configured language, preserving all existing features. Return summary and complete contents of only the approved files.

<!-- Iriska managed project instructions: begin -->
Реализуй только текущую согласованную подзадачу. Сохраняй существующую функциональность. Верни полный текст только разрешённых файлов. Не меняй существующие тесты, инструкции, зависимости или права.



<!-- Iriska managed project instructions: end -->

## IDE_HANDOFF_V1 — проверка передачи из VS Code

Сохраняй ручную константу `DEPOSIT_PERCENT = 30`, комментарий `IDE_HANDOFF_V1` и реализацию `deposit`. При расчёте остатка используй `quote(group, days) - deposit(group, days)`. В этом репозитории тесты импортируют `from src.quote import ...`; не используй `from quote import ...`. Не меняй существующие тесты, добавляй новые файлы unittest только по согласованному плану. Сохраняй целочисленную арифметику для больших чисел.
