public final class DepositPolicy {

    private DepositPolicy() {
    }

    public static long deposit(long total) {
        if (total <= 0) {
            throw new IllegalArgumentException("total must be positive");
        }
        return total / 100 * 30 + (total % 100 * 30 + 99) / 100;
    }

    public static long remaining(long total) {
        if (total <= 0) {
            throw new IllegalArgumentException("total must be positive");
        }
        return total - deposit(total);
    }
}
