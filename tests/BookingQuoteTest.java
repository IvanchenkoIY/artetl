public final class BookingQuoteTest {

    public void testRegular() {
        BookingQuote q = BookingQuote.create(5, 2);
        if (q.group() != 5) throw new AssertionError("group expected 5, got " + q.group());
        if (q.days() != 2) throw new AssertionError("days expected 2, got " + q.days());
        if (q.total() != 9000L) throw new AssertionError("total expected 9000, got " + q.total());
        if (q.deposit() != 2700L) throw new AssertionError("deposit expected 2700, got " + q.deposit());
        if (q.remaining() != 6300L) throw new AssertionError("remaining expected 6300, got " + q.remaining());
    }

    public void testInvalid() {
        try {
            BookingQuote.create(0, 1);
            throw new AssertionError("group=0 should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            BookingQuote.create(1, 0);
            throw new AssertionError("days=0 should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            BookingQuote.create(-1, 1);
            throw new AssertionError("negative group should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            BookingQuote.create(1, -1);
            throw new AssertionError("negative days should throw");
        } catch (IllegalArgumentException expected) {
        }
    }

    public void testLarge() {
        BookingQuote q = BookingQuote.create(1_000_000, 3);
        if (q.total() != 2_700_000_000L) throw new AssertionError("total expected 2700000000, got " + q.total());
        if (q.deposit() != 810_000_000L) throw new AssertionError("deposit expected 810000000, got " + q.deposit());
        if (q.remaining() != 1_890_000_000L) throw new AssertionError("remaining expected 1890000000, got " + q.remaining());
    }
}
