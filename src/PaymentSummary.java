public final class PaymentSummary {

    private PaymentSummary() {
    }

    public static String format(BookingQuote quote, long paid) {
        if (quote == null) {
            throw new IllegalArgumentException("quote must not be null");
        }
        if (paid < 0) {
            throw new IllegalArgumentException("paid must not be negative");
        }
        if (paid > quote.total()) {
            throw new IllegalArgumentException("paid must not exceed total");
        }
        return QuoteFormatter.format(quote) + "; paid=" + paid + "; due=" + (quote.total() - paid);
    }
}
