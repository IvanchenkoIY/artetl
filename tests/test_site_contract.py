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
