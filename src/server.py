import os, hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit
from pathlib import Path
from src.site import render_route
from src.registration import register
from src.booking import submit_booking

ASSETS={'/assets/mountain.jpg':'mountain.jpg','/assets/cabin.jpg':'cabin.jpg','/assets/quad.jpg':'quad.jpg'}
CSP="default-src 'none'; style-src 'unsafe-inline'; img-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'"

class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body, ctype='text/html; charset=utf-8', location=None):
        data=body if isinstance(body,bytes) else body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type',ctype)
        self.send_header('Content-Length',str(len(data)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Content-Security-Policy',CSP)
        if location:self.send_header('Location',location)
        self.end_headers();self.wfile.write(data)
    def do_GET(self):
        url=urlsplit(self.path)
        if url.path in ASSETS:
            p=Path(__file__).parent/'assets'/ASSETS[url.path]
            if p.is_file():self.reply(200,p.read_bytes(),'image/jpeg')
            else:self.reply(404,'Не найдено')
            return
        q=parse_qs(url.query)
        html=render_route(url.path, q.get('success')==['1'], q.get('kind',[''])[0] or None)
        if html is None:self.reply(404,'Не найдено')
        else:self.reply(200,html)
    def do_POST(self):
        if self.path!='/register' and self.path!='/booking':return self.reply(404,'Не найдено')
        origin=self.headers.get('Origin')
        if origin and urlsplit(origin).netloc!=self.headers.get('Host'):return self.reply(403,'Недопустимый источник')
        if self.headers.get('Content-Type','').split(';')[0]!='application/x-www-form-urlencoded':return self.reply(415,'Неверный формат')
        try:
            size=int(self.headers.get('Content-Length','0'))
            if self.path=='/register':
                if not 0<size<=2048:return self.reply(413,'Слишком большой запрос')
                data=parse_qs(self.rfile.read(size).decode('utf-8'),keep_blank_values=True,max_num_fields=4)
                if set(data)!={'name','email'} or any(len(v)!=1 for v in data.values()):raise ValueError()
                register(os.environ.get('SQLITE_PATH','registrations.sqlite3'),data['name'][0],data['email'][0])
                self.reply(303,'',location='/?success=1')
            else:
                if not 0<size<=4096:return self.reply(413,'Слишком большой запрос')
                data=parse_qs(self.rfile.read(size).decode('utf-8'),keep_blank_values=True,max_num_fields=6)
                if set(data)!={'kind','name','email','start_date','people'} or any(len(v)!=1 for v in data.values()):raise ValueError()
                try: people=int(data['people'][0])
                except ValueError: raise ValueError()
                submit_booking(os.environ.get('SQLITE_PATH','registrations.sqlite3'),data['kind'][0],data['name'][0],data['email'][0],data['start_date'][0],people)
                self.reply(303,'',location='/booking?success=1')
        except (ValueError,UnicodeError):return self.reply(400,'Проверьте данные. <a href="/">Вернуться</a>')
    def log_message(self,*args):pass

if __name__=='__main__':
    ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','8080'))),Handler).serve_forever()
