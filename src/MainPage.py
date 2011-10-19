from google.appengine.api import users
from google.appengine.ext import webapp
import os
#from IndexPage import IndexPage

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        path = os.path.join(os.path.split(__file__)[0], 'webpages/mainweb.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(file(path).read())
            
            
            
class Login(webapp.RequestHandler):
    
    def get(self):
        user = users.get_current_user()

        if user:
            self.redirect('/index')
#            self.response.out.write(
#                                    'Hello %s <a href="%s">Sign out</a><br>Is administrator: %s' % 
#                                    (user.nickname(), users.create_logout_url("/"), users.is_current_user_admin())
#                                    )
        else:
            self.redirect(users.create_login_url(self.request.uri))