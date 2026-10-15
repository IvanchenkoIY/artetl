"""HTTP entrypoint; behavior lives in the Iriska-editable src package."""
import os
from http.server import ThreadingHTTPServer
from src.server import Handler
if __name__=='__main__':
 ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','8080'))),Handler).serve_forever()
