from google.appengine.ext import webapp
from google.appengine.api import users
import os
import logging
class IndexPage(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        if user:
            logging.info('printing index page')
            path = os.path.join(os.path.split(__file__)[0], 'webpages/index.html')
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write(file(path).read())
        else:
            self.redirect(users.create_login_url(self.request.uri))        
        
        
class GetCross(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        logging.info('printing index page')
        path = os.path.join(os.path.split(__file__)[0], 'webpages/crossdomain.xml')
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(file(path).read())
        
        
class GetVerif(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        logging.info('printing index page')
        path = os.path.join(os.path.split(__file__)[0], 'webpages/google46e09675bd20e1bd.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(file(path).read())
        
        
class Robots(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        logging.info('printing index page')
        path = os.path.join(os.path.split(__file__)[0], 'webpages/robots.txt')
        self.response.headers['Content-Type'] = 'text/txt'
        self.response.out.write(file(path).read())        
        
        
class Sitemap(webapp.RequestHandler):
    
    
    def get(self):
        user = users.get_current_user()
        logging.info('printing index page')
        path = os.path.join(os.path.split(__file__)[0], 'webpages/sitemap.xml')
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(file(path).read())    
