public final class PaymentSummaryTest {

    public void testRegular() {
        BookingQuote q = BookingQuote.create(5, 2);
        String result = PaymentSummary.format(q, 2700);
        if (!result.equals("total=9000; deposit=2700; remaining=6300; paid=2700; due=6300")) {
            throw new AssertionError("expected 'total=9000; deposit=2700; remaining=6300; paid=2700; due=6300', got '" + result + "'");
        }
        String result0 = PaymentSummary.format(q, 0);
        if (!result0.equals("total=9000; deposit=2700; remaining=6300; paid=0; due=9000")) {
            throw new AssertionError("expected 'total=9000; deposit=2700; remaining=6300; paid=0; due=9000', got '" + result0 + "'");
        }
        String resultFull = PaymentSummary.format(q, 9000);
        if (!resultFull.equals("total=9000; deposit=2700; remaining=6300; paid=9000; due=0")) {
            throw new AssertionError("expected 'total=9000; deposit=2700; remaining=6300; paid=9000; due=0', got '" + resultFull + "'");
        }
    }

    public void testInvalid() {
        BookingQuote q = BookingQuote.create(5, 2);
        try {
            PaymentSummary.format(null, 0);
            throw new AssertionError("null quote should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            PaymentSummary.format(q, -1);
            throw new AssertionError("paid=-1 should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            PaymentSummary.format(q, 9001);
            throw new AssertionError("paid=9001 should throw");
        } catch (IllegalArgumentException expected) {
        }
    }

    public void testLarge() {
        BookingQuote q = BookingQuote.create(1_000_000, 3);
        String result = PaymentSummary.format(q, 810_000_000L);
        if (!result.equals("total=2700000000; deposit=810000000; remaining=1890000000; paid=810000000; due=1890000000")) {
            throw new AssertionError("expected 'total=2700000000; deposit=810000000; remaining=1890000000; paid=810000000; due=1890000000', got '" + result + "'");
        }
    }
}
