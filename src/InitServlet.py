from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from MainPage import MainPage
from MainPage import Login
from IndexPage import IndexPage
from IndexPage import GetCross
from IndexPage import GetVerif
from IndexPage import Robots
from IndexPage import Sitemap
from GetData import GetData
from DelData import DelData
from SetData import SetData

#${GOOGLE_APP_ENGINE}/dev_appserver.py

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/login', Login),
                                      ('/index',IndexPage),
                                      ('/DelData',DelData),
                                      ('/SetData',SetData),
                                      ('/getUserData',GetData),
                                      ('/sitemap.xml',Sitemap),
                                      ('/robots.txt',Robots),
                                      ('/crossdomain.xml',GetCross),
                                      ('/google46e09675bd20e1bd.html',GetVerif)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
