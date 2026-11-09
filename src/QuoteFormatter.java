public final class QuoteFormatter {

    private QuoteFormatter() {
    }

    public static String format(BookingQuote q) {
        if (q == null) {
            throw new IllegalArgumentException("BookingQuote must not be null");
        }
        return "total=" + q.total() + "; deposit=" + q.deposit() + "; remaining=" + q.remaining();
    }
}
