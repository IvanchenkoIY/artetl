import com.sun.net.httpserver.*;
import java.net.*;import java.nio.charset.StandardCharsets;import java.nio.file.*;import java.util.*;import java.util.concurrent.*;
public class Server {
 static final Path ROOT=Path.of("web");static final Path DATA=Path.of(System.getenv().getOrDefault("URAL_DATA","/tmp/ural-demo-data"));
 static final Map<String,String> PAGES=Map.of("/","index.html","/routes","routes.html","/trail","trail.html","/signup","signup.html","/about","about.html","/style.css","style.css","/assets/konzhak.jpg","assets/konzhak.jpg");
 static synchronized void save(Map<String,String> item)throws Exception{Files.createDirectories(DATA);String value=Base64.getEncoder().encodeToString(item.toString().getBytes(StandardCharsets.UTF_8));Files.writeString(DATA.resolve("requests.txt"),value+"\n",StandardOpenOption.CREATE,StandardOpenOption.APPEND);}
 static void send(HttpExchange x,int status,byte[] body,String kind)throws Exception{x.getResponseHeaders().set("Content-Type",kind);x.getResponseHeaders().set("X-Content-Type-Options","nosniff");x.getResponseHeaders().set("Cache-Control","no-store");x.sendResponseHeaders(status,body.length);try(var out=x.getResponseBody()){out.write(body);}}
 static void json(HttpExchange x,int status,String text)throws Exception{send(x,status,text.getBytes(StandardCharsets.UTF_8),"application/json; charset=utf-8");}
 static void handle(HttpExchange x){try{
  String path=x.getRequestURI().getPath();String method=x.getRequestMethod();
  if(method.equals("GET")){String file=PAGES.get(path);if(file==null){json(x,404,"{}");return;}String kind=file.endsWith("jpg")?"image/jpeg":file.endsWith("css")?"text/css; charset=utf-8":"text/html; charset=utf-8";send(x,200,Files.readAllBytes(ROOT.resolve(file)),kind);return;}
  if(!method.equals("POST")){json(x,405,"{}");return;}if(!path.equals("/signup")){json(x,404,"{}");return;}
  if(!x.getRequestHeaders().getFirst("Content-Type").startsWith("application/x-www-form-urlencoded")){json(x,415,"{}");return;}
  byte[] body=x.getRequestBody().readNBytes(4097);if(body.length>4096){json(x,413,"{}");return;}Map<String,String> fields=new HashMap<>();for(String part:new String(body,StandardCharsets.UTF_8).split("&")){String[] kv=part.split("=",2);if(kv.length!=2)throw new IllegalArgumentException();String key=URLDecoder.decode(kv[0],StandardCharsets.UTF_8);if(fields.put(key,URLDecoder.decode(kv[1],StandardCharsets.UTF_8))!=null)throw new IllegalArgumentException();}
  if(!fields.keySet().equals(Set.of("name","email","route")))throw new IllegalArgumentException();save(Booking.register(fields));json(x,201,"{\"demo\":true,\"saved\":true}");
 }catch(IllegalArgumentException e){try{json(x,400,"{}");}catch(Exception ignored){}}catch(UnsupportedOperationException e){try{json(x,501,"{}");}catch(Exception ignored){}}catch(Exception e){try{json(x,500,"{}");}catch(Exception ignored){}}finally{x.close();}}
 public static void main(String[] args)throws Exception{var server=HttpServer.create(new InetSocketAddress("0.0.0.0",args.length==0?8080:Integer.parseInt(args[0])),0);server.createContext("/",Server::handle);server.setExecutor(Executors.newFixedThreadPool(4));server.start();System.out.println(server.getAddress().getPort());System.out.flush();}
}
