import java.nio.file.*;
import java.net.*;
import java.util.*;
import java.lang.reflect.*;
import javax.tools.ToolProvider;
public final class Check {
    static String xml(String s) { return s.replace("&", "&amp;").replace("<", "&lt;").replace("\"", "&quot;"); }
    public static void main(String[] args) throws Exception {
        Path output = Files.createTempDirectory("iriska-java-tests-");
        List<String> compile = new ArrayList<>(List.of("-encoding", "UTF-8", "-d", output.toString()));
        List<String> classes = new ArrayList<>();
        for (String folder : List.of("src", "tests")) {
            try (var files = Files.walk(Path.of(folder))) {
                for (Path file : files.filter(p -> p.toString().endsWith(".java") && !p.getFileName().toString().equals("Check.java")).sorted().toList()) {
                    compile.add(file.toString());
                    if (file.getFileName().toString().endsWith("Test.java")) classes.add(file.getFileName().toString().replace(".java", ""));
                }
            }
        }
        int result = ToolProvider.getSystemJavaCompiler().run(null, null, null, compile.toArray(String[]::new));
        if (result != 0) throw new AssertionError("Compilation failed: " + result);
        int count = 0, failures = 0; StringBuilder body = new StringBuilder();
        try (var loader = new URLClassLoader(new URL[] {output.toUri().toURL()})) {
            for (String name : classes) {
                Class<?> type = loader.loadClass(name);
                for (Method method : Arrays.stream(type.getDeclaredMethods()).sorted(Comparator.comparing(Method::getName)).toList()) {
                    if (!method.getName().startsWith("test") || method.getParameterCount() != 0 || !Modifier.isPublic(method.getModifiers())) continue;
                    count++; body.append("<testcase classname=\"").append(xml(name)).append("\" name=\"").append(xml(method.getName())).append("\">");
                    try { method.invoke(type.getDeclaredConstructor().newInstance()); System.out.println(name + "#" + method.getName() + " PASS"); }
                    catch (Throwable e) { failures++; Throwable cause = e instanceof InvocationTargetException ? e.getCause() : e; body.append("<failure message=\"").append(xml(cause.toString())).append("\"/>"); cause.printStackTrace(); }
                    body.append("</testcase>\n");
                }
            }
        }
        Path reports = Path.of("/tmp/iriska-test-reports"); Files.createDirectories(reports);
        Files.writeString(reports.resolve("tests.xml"), "<testsuite name=\"tour\" tests=\"" + count + "\" failures=\"" + failures + "\" errors=\"0\" skipped=\"0\">\n" + body + "</testsuite>\n");
        if (count == 0 || failures != 0) throw new AssertionError("tests=" + count + ", failures=" + failures);
        System.out.println("All " + count + " tests passed");
    }
}
