public final class TourPriceTest {
    public void testRegular() { if (TourPrice.quote(1, 1) != 1000 || TourPrice.quote(5, 2) != 9000) throw new AssertionError("regular price"); }
    public void testInvalid() { try { TourPrice.quote(0, 1); throw new AssertionError("invalid group accepted"); } catch (IllegalArgumentException expected) {} }
    public void testLarge() { if (TourPrice.quote(1_000_000, 3) != 2_700_000_000L) throw new AssertionError("long precision"); }
}
