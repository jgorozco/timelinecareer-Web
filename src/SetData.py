import simplejson
from frwk.UserModel import *
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import Request
import logging
class SetData(webapp.RequestHandler):

    def get(self):
        logging.info('getting data for index page')
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"error":"get not handler"}')

    
    def post(self):
        listArguments=self.request.arguments()
        if len(listArguments)>0:#analizamos el argumento
            argumentData=listArguments.pop()
            logging.info('______ '+self.request.get(argumentData)+' ________')
            if argumentData=='type' : #el argumento esta bien
                argumento=self.request.get(argumentData);
                if argumento=='UserData':
                    self.setUserData()
                if argumento=='Proyects':
                    self.setProyects()
                if argumento=='Themes':
                    self.setTheme()
                if argumento=='Categories':
                    self.setTags()
            else:#el argumento esta mal
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.out.write('{"status":"ERROR[bad argument]"}')                
        else:#sacamos todos los datos
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('{"status":"ERROR[no argument]"}')
            
    def setProyects(self):# todos los proyects
        logging.info('______ setProjects ________')
        listado=self.request.body;
  #      logging.info(self.request.body);
        proyectos=simplejson.loads(self.request.body)
        borrarTodas=Proyect.gql("WHERE MyUser = :1",users.get_current_user())
        for proy in borrarTodas:
            proy.delete() 
        for proy in proyectos:
            myProyect=Proyect();
            myProyect.MyUser=users.get_current_user()
            myProyect.LoadFromJSON(simplejson.dumps(proy))
   #         logging.info("elemento["+myProyect.Name+"] ["+myProyect.Category+"]");
            while myProyect.is_saved()!=True:
                myProyect.put()
 #       logging.info("elementos en category:"+str(Proyect.all().count()));
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"status":"ok"}')      
        
    def setTheme(self): #todas las themes
        logging.info('______ setTheme ________')
        logging.info(self.request.body);
        mytheme=Theme.gql("WHERE MyUser = :1",
                               users.get_current_user())
        for theme in mytheme:
            theme.delete()
            logging.info('los datos ya estan creados')
        else:
             theme=Theme()
             theme.MyUser=users.get_current_user()
        theme.LoadFromJSON(self.request.body)     
        theme.put()
        logging.info('getting data for index page post:'+self.request.body)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"status":"ok"}')           
    def setTags(self): # todas las tags  
        logging.info('______ setTags ________')
        listado=self.request.body;
        logging.info(self.request.body);
        categoryList=simplejson.loads(self.request.body)
        borrarTodas=Tags.gql("WHERE MyUser = :1",users.get_current_user())
        for categ in borrarTodas:
            categ.delete() 
        for category in categoryList:
            myCategory=Tags();
            myCategory.MyUser=users.get_current_user()
            myCategory.LoadFromJSON(simplejson.dumps(category))
            logging.info("elemento["+myCategory.Name+"] ["+myCategory.Color+"]");
            while myCategory.is_saved()!=True:
                myCategory.put()
        logging.info("elementos en category"+str(Tags.all().count()));
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"status":"ok"}')      
        
    def setAll(self): # todos los datos, creo q no aplica
        logging.info('______ setAll ________')
    
    def setUserData(self):
        logging.info('______ setCOSAS ________')
        myUserData=UserData.gql("WHERE MyUser = :1",
                               users.get_current_user())
        if myUserData.count()>0:
            newUserData=myUserData.get()    
            logging.info('los datos ya estan creados')
        else:
             newUserData=UserData()
             newUserData.MyUser=users.get_current_user()
        newUserData.LoadFromJSON(self.request.body)     
        newUserData.put()
        logging.info('getting data for index page post:'+newUserData.Name)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"status":"ok"}')    

        