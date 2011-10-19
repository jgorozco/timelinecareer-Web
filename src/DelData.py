from google.appengine.ext import webapp
from google.appengine.ext.webapp import Request
import logging
class DelData(webapp.RequestHandler):
    
    def get(self):
        logging.info('getting data for index page')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"error":"get not handler"}')

    
    def post(self):
        logging.info('getting data for index page')