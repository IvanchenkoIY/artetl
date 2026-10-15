from html.parser import HTMLParser
import unittest
from src.page import render_page
class Structure(HTMLParser):
 def __init__(self):
  super().__init__();self.stack=[];self.targets=set();self.links=[];self.labels=set();self.inputs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='label' and a.get('for'):self.labels.add(a['for'])
  if tag=='form':self.targets.update(x.get('id') for t,x in [*self.stack,(tag,a)] if x.get('id'))
  if tag=='input':self.inputs.append((a,any(t=='label' for t,x in self.stack)))
  if tag not in ('meta','link','input','br','hr','img','area','base','col','embed','param','source','track','wbr'):self.stack.append((tag,a))
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
class SiteContract(unittest.TestCase):
 def test_registration_link(self):
  s=Structure();s.feed(render_page())
  self.assertTrue(any(h.startswith('#') and len(h)>1 and h[1:] in s.targets for h in s.links),'Нужна действующая ссылка на форму регистрации')
 def test_accessible_inputs(self):
  s=Structure();s.feed(render_page())
  for a,wrapped in s.inputs:
   if a.get('name') in ('name','email'):self.assertTrue(wrapped or a.get('id') in s.labels)

# Added by the acceptance reviewer before the cabins iteration. Read-only to agents.
import hashlib, os, tempfile, threading
from http.server import ThreadingHTTPServer
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from pathlib import Path

class SiteRoutes(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  from src.server import Handler
  cls.temp=tempfile.TemporaryDirectory();cls.previous=os.environ.get('SQLITE_PATH');os.environ['SQLITE_PATH']=str(Path(cls.temp.name)/'data.sqlite3')
  cls.server=ThreadingHTTPServer(('127.0.0.1',0),Handler);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start();cls.origin='http://127.0.0.1:'+str(cls.server.server_port)
 @classmethod
 def tearDownClass(cls):
  cls.server.shutdown();cls.server.server_close();cls.thread.join(3);cls.temp.cleanup()
  if cls.previous is None:os.environ.pop('SQLITE_PATH',None)
  else:os.environ['SQLITE_PATH']=cls.previous
 def get(self,path):
  with urlopen(self.origin+path,timeout=3) as r:return r.status,r.headers,r.read()
 def test_cabins_navigation(self):
  for path in ['/', '/cabins']:
   status,headers,body=self.get(path);self.assertEqual(status,200);html=body.decode();self.assertIn('viewport',html)
   p=Structure();p.feed(html)
   self.assertIn('/',p.links);self.assertIn('/cabins',p.links)
   self.assertNotIn('<script',html.lower());self.assertIn('form-action',headers['Content-Security-Policy'])
  html=self.get('/cabins')[2].decode();self.assertIn('Домики',html);self.assertIn('/assets/cabin.jpg',html)
  for word in ['Brian M. Powell','CC BY-SA','https://creativecommons.org/licenses/by-sa/3.0/']:
   self.assertIn(word,html)
  self.assertIn('иллюстрац',html.lower());self.assertIn('демонстрац',html.lower())
 def test_static_assets_safe(self):
  hashes={'mountain.jpg':'091b1d2ec6e8d36483f1eb0628c0ad353ea2bc456b73e79f4e48dfbb51e29190','cabin.jpg':'3f5b9f271801f3afbf130b2cbb0ebdea50ee1ffc3c509ab604ec877d960bed0d','quad.jpg':'8164fdce8c23d3a037d9bcbb34e60779d090fe62993c55912995305bb35b93b7'}
  for name,digest in hashes.items():
   status,headers,body=self.get('/assets/'+name);self.assertEqual(status,200);self.assertEqual(headers.get_content_type(),'image/jpeg');self.assertEqual(hashlib.sha256(body).hexdigest(),digest)
  self.assertIn("img-src 'self'",self.get('/cabins')[1]['Content-Security-Policy'])
  for path in ['/not-a-page','/assets/../../README.md','/assets/%2e%2e/app.py','/assets/credits.json','/registrations.sqlite3']:
   with self.assertRaises(HTTPError) as e:self.get(path)
   self.assertEqual(e.exception.code,404)
