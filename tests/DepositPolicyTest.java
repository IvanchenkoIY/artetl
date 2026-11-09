public final class DepositPolicyTest {

    public void testRegular() {
        if (DepositPolicy.deposit(1000) != 300) {
            throw new AssertionError("deposit(1000) expected 300");
        }
        if (DepositPolicy.remaining(1000) != 700) {
            throw new AssertionError("remaining(1000) expected 700");
        }
        if (DepositPolicy.deposit(1) != 1) {
            throw new AssertionError("deposit(1) expected 1");
        }
        if (DepositPolicy.remaining(1) != 0) {
            throw new AssertionError("remaining(1) expected 0");
        }
    }

    public void testInvalid() {
        try {
            DepositPolicy.deposit(0);
            throw new AssertionError("deposit(0) should throw");
        } catch (IllegalArgumentException expected) {
        }
        try {
            DepositPolicy.deposit(-1);
            throw new AssertionError("deposit(-1) should throw");
        } catch (IllegalArgumentException expected) {
        }
    }

    public void testLarge() {
        long max = Long.MAX_VALUE;
        long dep = DepositPolicy.deposit(max);
        if (dep != 2767011611056432743L) {
            throw new AssertionError("deposit(Long.MAX_VALUE) expected 2767011611056432743L, got " + dep);
        }
        long rem = DepositPolicy.remaining(max);
        if (dep + rem != max) {
            throw new AssertionError("deposit + remaining should equal Long.MAX_VALUE");
        }
    }
}
