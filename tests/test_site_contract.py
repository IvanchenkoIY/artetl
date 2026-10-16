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
 def test_activity_pages(self):
  for path in ['/', '/cabins', '/quad', '/views']:
   html=self.get(path)[2].decode();p=Structure();p.feed(html)
   for link in ['/', '/cabins', '/quad', '/views']:self.assertIn(link,p.links)
  quad=self.get('/quad')[2].decode();views=self.get('/views')[2].decode()
  for text in ['/assets/quad.jpg','Kenneth Allen','CC BY-SA','https://creativecommons.org/licenses/by-sa/2.0/']:
   self.assertIn(text,quad)
  for text in ['/assets/mountain.jpg','Makarenko Sasha','CC BY-SA','https://creativecommons.org/licenses/by-sa/3.0/']:
   self.assertIn(text,views)
  self.assertIn('квадро',quad.lower());self.assertTrue('обзор' in views.lower() or 'панорам' in views.lower())
  self.assertIn('иллюстрац',quad.lower());self.assertIn('демонстрац',quad.lower());self.assertIn('демонстрац',views.lower())
  for html in [quad,views]:self.assertNotIn('<script',html.lower())

import sqlite3
from datetime import date,timedelta
class SelectedOptions(HTMLParser):
 def __init__(self):super().__init__();self.values=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='option' and 'selected' in a:self.values.append(a.get('value'))
class BookingContract(unittest.TestCase):
 def test_booking_persistence(self):
  from src.booking import submit_booking
  from src.registration import register
  with tempfile.TemporaryDirectory() as temp:
   db=Path(temp)/'data.sqlite3';register(db,'Прежняя запись','old@example.test')
   day=(date.today()+timedelta(days=30)).isoformat()
   for kind in ['hike','cabin','quad']:submit_booking(db,kind,'  Тестовый турист  ',' test@example.test ',day,2)
   with sqlite3.connect(db) as c:
    rows=c.execute('SELECT kind,name,email,start_date,people FROM bookings ORDER BY rowid').fetchall()
    self.assertEqual(rows,[(kind,'Тестовый турист','test@example.test',day,2) for kind in ['hike','cabin','quad']])
    self.assertEqual(c.execute('SELECT name,email FROM registrations').fetchall(),[('Прежняя запись','old@example.test')])
 def test_booking_invalid_input(self):
  from src.booking import submit_booking
  with tempfile.TemporaryDirectory() as temp:
   db=Path(temp)/'data.sqlite3';day=(date.today()+timedelta(days=30)).isoformat();good=['hike','Тестовый турист','test@example.test',day,2]
   submit_booking(db,*good)
   for index,values in [(0,['unknown','',"hike'); DROP TABLE bookings;--"]),(1,['','x','x'*81]),(2,['a','a@@b.test','a b@c.test','x'*255]),(3,['', '2026-99-99',day.replace('-',''),(date.today()-timedelta(days=1)).isoformat()]),(4,[0,13,-1,1.5,True,'2'])]:
    for value in values:
     args=good.copy();args[index]=value
     with self.assertRaises(ValueError):submit_booking(db,*args)
   with sqlite3.connect(db) as c:self.assertEqual(c.execute('SELECT COUNT(*) FROM bookings').fetchone()[0],1)
 def test_booking_fragment(self):
  from src.booking import render_booking
  for kind in ['hike','cabin','quad']:
   html=render_booking(kind,False);p=Structure();p.feed(html);selected=SelectedOptions();selected.feed(html);self.assertEqual(selected.values,[kind])
   self.assertIn('action="/booking"',html);self.assertIn('method="post"',html);self.assertNotIn('Заявка принята',html)
   for field in ['name','email','start_date','people']:
    matching=[(a,wrapped) for a,wrapped in p.inputs if a.get('name')==field];self.assertEqual(len(matching),1)
    a,wrapped=matching[0];self.assertTrue(wrapped or a.get('id') in p.labels);self.assertIn('required',a)
   self.assertIn('name="kind"',html);self.assertIn('Заявка принята',render_booking(kind,True))
  self.assertNotIn('<script',render_booking('<script>alert(1)</script>',False).lower())

from urllib.parse import urlencode
from urllib.request import build_opener, HTTPRedirectHandler
class NoRedirect(HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None
class BookingHTTP(SiteRoutes):
 def post(self,path,data,origin=None,content_type='application/x-www-form-urlencoded'):
  body=urlencode(data).encode() if not isinstance(data,bytes) else data
  req=Request(self.origin+path,data=body,headers={'Content-Type':content_type,'Origin':origin or self.origin})
  try:
   with build_opener(NoRedirect()).open(req,timeout=3) as r:return r.status,r.headers,r.read()
  except HTTPError as e:return e.code,e.headers,e.read()
 def count(self):
  with sqlite3.connect(os.environ['SQLITE_PATH']) as c:return c.execute('SELECT COUNT(*) FROM bookings').fetchone()[0]
 def test_booking_http_success_and_navigation(self):
  for path in ['/', '/cabins','/quad','/views','/booking']:
   status,headers,body=self.get(path);self.assertEqual(status,200);s=Structure();s.feed(body.decode())
   for link in ['/', '/cabins','/quad','/views','/booking']:self.assertIn(link,s.links)
  for kind in ['hike','cabin','quad']:
   html=self.get('/booking?kind='+kind)[2].decode();self.assertIn('action="/booking"',html)
   day=(date.today()+timedelta(days=30)).isoformat()
   code,headers,body=self.post('/booking',{'kind':kind,'name':'HTTP Test','email':'http@example.test','start_date':day,'people':'2'})
   self.assertEqual(code,303);self.assertTrue(headers['Location'].startswith('/booking?'))
   self.assertIn('Заявка принята',self.get(headers['Location'])[2].decode())
  with sqlite3.connect(os.environ['SQLITE_PATH']) as c:
   rows=c.execute("SELECT kind,people FROM bookings WHERE email=?",('http@example.test',)).fetchall()
   self.assertEqual(rows,[('hike',2),('cabin',2),('quad',2)])
  code,headers,_=self.post('/register',{'name':'Old Form','email':'old-http@example.test'});self.assertEqual(code,303)
  with sqlite3.connect(os.environ['SQLITE_PATH']) as c:self.assertIn('old-http@example.test',str(c.execute('SELECT email FROM registrations').fetchall()))
 def test_booking_http_invalid_no_insert(self):
  day=(date.today()+timedelta(days=30)).isoformat();good={'kind':'hike','name':'HTTP Guard','email':'guard@example.test','start_date':day,'people':'2'}
  self.assertEqual(self.post('/booking',good)[0],303);count=self.count()
  for field,value in [('kind','bad'),('name',''),('email','bad'),('start_date','yesterday'),('people','2.5'),('people','0'),('people','13')]:
   bad=good.copy();bad[field]=value;self.assertEqual(self.post('/booking',bad)[0],400)
  self.assertEqual(self.post('/booking',urlencode(good).encode()+b'&kind=quad')[0],400)
  self.assertEqual(self.post('/booking',good,origin='https://foreign.invalid')[0],403)
  self.assertEqual(self.post('/booking',b'{}',content_type='application/json')[0],415)
  self.assertEqual(self.post('/booking',b'x'*5000)[0],413)
  self.assertEqual(self.post('/missing',good)[0],404);self.assertEqual(self.count(),count)
  self.assertNotIn('<script>',self.get('/booking?kind=%3Cscript%3E')[2].decode().lower())

class HomeEditorial(unittest.TestCase):
 def test_demo_copy_and_registration_preserved(self):
  html=render_page();lower=html.lower();self.assertIn('демонстрац',lower)
  for unsupported in ['среднем урале','3–5 часов','3-5 часов','2–3 недели','2-3 недели']:self.assertNotIn(unsupported,lower)
  self.assertIn('Конжаковский',html);self.assertIn('action="/register"',html)
  s=Structure();s.feed(html);self.assertTrue(any(h.startswith('#') and h[1:] in s.targets for h in s.links))
  self.assertNotIn('Заявка принята',html);self.assertIn('Заявка принята',render_page(True))

class BookingPresentation(unittest.TestCase):
 def test_human_labels_and_form_limits(self):
  from src.booking import render_booking
  html=render_booking('cabin');p=Structure();p.feed(html)
  for label in ['Поход','Домик','Квадротур']:self.assertIn(label,html)
  for token in ['>hike</option>','>cabin</option>','>quad</option>']:self.assertNotIn(token,html)
  fields={a.get('name'):a for a,_ in p.inputs}
  self.assertEqual(fields['name'].get('maxlength'),'80');self.assertEqual(fields['email'].get('maxlength'),'254')
  self.assertEqual(fields['people'].get('min'),'1');self.assertEqual(fields['people'].get('max'),'12')
  self.assertIn('демонстрац',html.lower());self.assertNotIn('<script',html.lower())

class BookingHeading(unittest.TestCase):
 def test_one_booking_heading_and_existing_form(self):
  from src.site import render_route
  class Headings(HTMLParser):
   def __init__(self):super().__init__();self.values=[];self.inside=False
   def handle_starttag(self,tag,attrs):
    if tag=='h1':self.values.append('');self.inside=True
   def handle_data(self,data):
    if self.inside:self.values[-1]+=data
   def handle_endtag(self,tag):
    if tag=='h1':self.inside=False
  for kind in ['hike','cabin','quad']:
   for success in [False,True]:
    html=render_route('/booking',success=success,kind=kind);h=Headings();h.feed(html)
    self.assertEqual(len(h.values),1,'Страница заявки должна иметь ровно один заголовок h1')
    self.assertIn('заяв',h.values[0].lower());self.assertIn('action="/booking"',html)
    s=Structure();s.feed(html)
    for link in ['/','/cabins','/quad','/views','/booking']:self.assertIn(link,s.links)
