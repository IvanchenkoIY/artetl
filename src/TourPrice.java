public final class TourPrice {
    private TourPrice() {}
    public static long quote(int group, int days) {
        if (group <= 0 || days <= 0) throw new IllegalArgumentException("positive group and days required");
        return Math.multiplyExact(Math.multiplyExact((long) group, days), group >= 5 ? 900L : 1000L);
    }
}
