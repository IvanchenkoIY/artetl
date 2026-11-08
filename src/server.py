from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs
import json, os, sys, threading
from booking import register
ROOT=Path(__file__).resolve().parent.parent/'web'
DATA=Path(os.environ.get('URAL_DATA','/tmp/ural-demo-data'))
LOCK=threading.Lock()
PAGES={'/':'index.html','/routes':'routes.html','/trail':'trail.html','/signup':'signup.html','/about':'about.html','/style.css':'style.css','/assets/konzhak.jpg':'assets/konzhak.jpg'}
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def send(self,status,body,kind='application/json; charset=utf-8'):
        self.send_response(status); self.send_header('Content-Type',kind)
        self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Cache-Control','no-store')
        self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        path=urlsplit(self.path).path
        if path not in PAGES:return self.send(404,b'{}')
        file=ROOT/PAGES[path]
        kind='image/jpeg' if file.suffix=='.jpg' else 'text/css; charset=utf-8' if file.suffix=='.css' else 'text/html; charset=utf-8'
        self.send(200,file.read_bytes(),kind)
    def do_POST(self):
        if urlsplit(self.path).path!='/signup':return self.send(404,b'{}')
        try:
            length=int(self.headers.get('Content-Length','0'))
            if length<1 or length>4096:return self.send(413,b'{}')
            if self.headers.get('Content-Type','').split(';')[0]!='application/x-www-form-urlencoded':return self.send(415,b'{}')
            fields=parse_qs(self.rfile.read(length).decode('utf-8'),keep_blank_values=True)
            if set(fields)!={'name','email','route'} or any(len(v)!=1 for v in fields.values()):raise ValueError()
            item=register(*(fields[k][0] for k in ['name','email','route']))
            with LOCK:
                DATA.mkdir(parents=True,exist_ok=True)
                with (DATA/'requests.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(item,ensure_ascii=False)+'\n')
            self.send(201,b'{"demo":true,"saved":true}')
        except (ValueError,UnicodeError):self.send(400,b'{"error":"invalid fields"}')
        except NotImplementedError:self.send(501,b'{"error":"not implemented"}')
    def do_PUT(self):self.send(405,b'{}')
if __name__=='__main__':
    server=ThreadingHTTPServer(('0.0.0.0',int(sys.argv[1]) if len(sys.argv)>1 else 8080),Handler)
    print(server.server_address[1],flush=True);server.serve_forever()
