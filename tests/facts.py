from pathlib import Path
import subprocess,sys,os,tempfile,urllib.request,re
root=Path(__file__).resolve().parent.parent;name=sys.argv[1];path={'index':'/','routes':'/routes','trail':'/trail'}[name]
with tempfile.TemporaryDirectory() as data:
 proc=subprocess.Popen([sys.executable,str(root/'src/server.py'),'0'],stdout=subprocess.PIPE,text=True,env={**os.environ,'URAL_DATA':data})
 try:
  port=proc.stdout.readline().strip();html=urllib.request.urlopen('http://127.0.0.1:'+port+path,timeout=10).read().decode();text=re.sub(r'(?is)<!--.*?-->|<script\b.*?</script>|<style\b.*?</style>',' ',html);text=re.sub(r'<[^>]*>',' ',text);text=' '.join(text.split()).lower()
  assert 'северный урал' in text,(name,'explicit canonical region label')
  if name=='routes':assert 'южный урал' in text
  else:assert '1569' in text,(name,'verified height')
  for forbidden in ['1565','конжаково','высочайшая точка северного урала','высшая точка северного урала','самая высокая вершина северного урала']:
   assert forbidden not in text,(name,'unsupported statement',forbidden)
  print('PASS grounded visible geography',name)
 finally:proc.terminate();proc.wait(timeout=5)
