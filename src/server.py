"""Small transport scaffold; page and persistence are implemented by Iriska."""
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit
from src.page import render_page
from src.registration import register

class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body, location=None):
        data=body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Content-Length',str(len(data)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Content-Security-Policy',"default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'")
        if location:self.send_header('Location',location)
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        url=urlsplit(self.path)
        if url.path!='/':return self.reply(404,'Не найдено')
        self.reply(200,render_page(parse_qs(url.query).get('success')==['1']))
    def do_POST(self):
        if self.path!='/register':return self.reply(404,'Не найдено')
        origin=self.headers.get('Origin')
        if origin and urlsplit(origin).netloc!=self.headers.get('Host'):return self.reply(403,'Недопустимый источник')
        if self.headers.get('Content-Type','').split(';')[0]!='application/x-www-form-urlencoded':return self.reply(415,'Неверный формат')
        try:
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=2048:return self.reply(413,'Слишком большой запрос')
            data=parse_qs(self.rfile.read(size).decode('utf-8'),keep_blank_values=True,max_num_fields=4)
            if set(data)!={'name','email'} or any(len(v)!=1 for v in data.values()):raise ValueError()
            register(os.environ.get('SQLITE_PATH','registrations.sqlite3'),data['name'][0],data['email'][0])
        except (ValueError,UnicodeError):return self.reply(400,'Проверьте имя и email. <a href="/">Вернуться</a>')
        self.reply(303,'',location='/?success=1')
    def log_message(self,*args):pass

if __name__=='__main__':
    ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','8080'))),Handler).serve_forever()
