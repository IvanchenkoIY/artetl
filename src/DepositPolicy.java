public final class DepositPolicy {
    // IDE_JAVA_HANDOFF_V1: бизнес-ставка выделена разработчиком.
    public static final long DEPOSIT_PERCENT = 30;

    private DepositPolicy() {
    }

    public static long deposit(long total) {
        if (total <= 0) {
            throw new IllegalArgumentException("total must be positive");
        }
        return total / 100 * DEPOSIT_PERCENT + (total % 100 * DEPOSIT_PERCENT + 99) / 100;
    }

    public static long remaining(long total) {
        if (total <= 0) {
            throw new IllegalArgumentException("total must be positive");
        }
        return total - deposit(total);
    }
}
