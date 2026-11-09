public record BookingQuote(int group, int days, long total, long deposit, long remaining) {

    public static BookingQuote create(int group, int days) {
        long total = TourPrice.quote(group, days);
        long deposit = DepositPolicy.deposit(total);
        long remaining = DepositPolicy.remaining(total);
        return new BookingQuote(group, days, total, deposit, remaining);
    }
}
