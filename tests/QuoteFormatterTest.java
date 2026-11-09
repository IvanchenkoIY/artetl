public final class QuoteFormatterTest {

    public void testRegular() {
        BookingQuote q = BookingQuote.create(1, 1);
        String result = QuoteFormatter.format(q);
        if (!result.equals("total=1000; deposit=300; remaining=700")) {
            throw new AssertionError("expected 'total=1000; deposit=300; remaining=700', got '" + result + "'");
        }
    }

    public void testInvalid() {
        try {
            QuoteFormatter.format(null);
            throw new AssertionError("null should throw IllegalArgumentException");
        } catch (IllegalArgumentException expected) {
        }
    }

    public void testLarge() {
        BookingQuote q = BookingQuote.create(1_000_000, 3);
        String result = QuoteFormatter.format(q);
        if (!result.equals("total=2700000000; deposit=810000000; remaining=1890000000")) {
            throw new AssertionError("expected 'total=2700000000; deposit=810000000; remaining=1890000000', got '" + result + "'");
        }
    }
}
