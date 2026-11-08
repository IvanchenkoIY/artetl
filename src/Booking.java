import java.util.*;

public final class Booking {
    private static final Set<String> ROUTES = Set.of("konzhak", "taganay", "iremel");

    private Booking() {}

    public static Map<String, String> register(Map<String, String> fields) {
        if (fields == null) throw new IllegalArgumentException("fields");
        String name = fields.get("name");
        String email = fields.get("email");
        String route = fields.get("route");

        if (name == null) throw new IllegalArgumentException("name");
        name = name.trim();
        if (name.isEmpty() || name.length() > 100) throw new IllegalArgumentException("name");

        if (email == null) throw new IllegalArgumentException("email");
        email = email.trim();
        if (email.length() > 254) throw new IllegalArgumentException("email");
        int at = email.indexOf('@');
        if (at <= 0 || at == email.length() - 1) throw new IllegalArgumentException("email");
        String domain = email.substring(at + 1);
        if (!domain.contains(".")) throw new IllegalArgumentException("email");

        if (route == null || !ROUTES.contains(route)) throw new IllegalArgumentException("route");

        Map<String, String> result = new LinkedHashMap<>();
        result.put("name", name);
        result.put("email", email);
        result.put("route", route);
        return result;
    }
}
