from frwk.UserModel import *
from google.appengine.ext import webapp
from google.appengine.ext.webapp import Request
from google.appengine.api import users
from google.appengine.api.users import User
import logging
import simplejson
class GetData(webapp.RequestHandler):
    numero = 2
    
    def get(self):
        logging.info('getting data for index page')
        listArguments=self.request.arguments()
        if len(listArguments)>0:#analizamos el argumento
            argumentData=listArguments.pop()
            if argumentData=='type' : #el argumento esta bien
                argumento=self.request.get(argumentData)
                logging.info('GETTER='+argumento)   
                if argumento=='all':
                    
                    if len(listArguments)>0:
                        mail=listArguments.pop()
                        self.getAllUserData(self.request.get(mail)) 
                    else:    
                        self.response.headers['Content-Type'] = 'text/plain'
                        self.response.out.write('{"status":"ERROR[bad argument]"}')  
                if argumento=='UserData':
                    self.getUserData()
                if argumento=='Proyects':
                    self.getProyects()
                if argumento=='Themes':
                    self.getTheme()
                if argumento=='Categories':
                    self.getTags()
            else:#el argumento esta mal
                self.response.headers['Content-Type'] = 'text/plain'
                self.response.out.write('{"status":"ERROR[bad argument]"}')                
        else:#sacamos todos los datos
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('{"status":"ERROR[no argument]"}')
    
    def post(self):
        user= users.get_current_user()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('{"status":"no_response"}')
       
    def getAllUserData(self,mail):
        logging.info('______ getAlldata _____{'+str(mail)+'}___')
        user=User(mail)
        #getUser
        userData=UserData()
        theme=Theme()
        tags=ListDTO()
        proyects=ListDTO()
        ##user
        myUserData=UserData.gql("WHERE MyUser = :1",user)  
        if myUserData.count()>0:
            userData=myUserData.get()
  #          logging.info('____'+str(userData.Name).encode('UTF-8','ignore'))
        ##projects
        projectGroup=Proyect.gql("WHERE MyUser = :1",user)
        salida=''
        if projectGroup.count>0:
            proyects=ListDTO(projectGroup)
        ##theme
        mytheme=Theme.gql("WHERE MyUser = :1",user)
        if mytheme.count()>0:
            theme=mytheme.get()
        ##tags
        myTags=Tags.gql("WHERE MyUser = :1",user)
        if myTags.count>0:
            tags=ListDTO(myTags)        
        if myUserData.count()>0:
            completeData=CompleteData(userData,theme,tags,proyects)        
            ##TODO mirar esto para que devuelva todo el json
            self.response.headers['Content-Type'] = 'text/plain'
            logging.info('___->'+str(completeData.SaveToJSON()))
            self.response.out.write(completeData.SaveToJSON())
        else:            
            self.response.headers['Content-Type'] = 'text/plain'        
            self.response.out.write('{"status":"ERROR[bad argument]"}'); 
        
     
        
        
    def getProyects(self):
        logging.info('______ getProyects ________')
        user= users.get_current_user()
        projectGroup=Proyect.gql("WHERE MyUser = :1",users.get_current_user())
        salida=''
        if projectGroup.count>0:
            listadoSerializable=ListDTO(projectGroup)
            salida=listadoSerializable.Serialize()
        else:
            salida=str(simplejson.dumps(list(projectGroup)))
        logging.info('Tenemos ESTOS elementos:'+str(projectGroup.count())+"generamos"+salida)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(salida)            
    def getTheme(self):
        logging.info('______ getTheme ________')
        user= users.get_current_user()
        mytheme=Theme.gql("WHERE MyUser = :1",users.get_current_user())
        if mytheme.count()>0:
            theme=mytheme.get()
            logging.info('los datos ya estan creados')
        else :
            theme=Theme()
        logging.info('El objeto en ddbb:'+str(theme.SaveToJSON()))
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(theme.SaveToJSON())    
                    
    def getTags(self):    
        logging.info('______ getTags ________')
        user= users.get_current_user()
        listElements=[];
        myTags=Tags.gql("WHERE MyUser = :1",users.get_current_user())
        salida=''
        if myTags.count>0:
            listadoSerializable=ListDTO(myTags)
            salida=listadoSerializable.Serialize()
        else:
            salida=str(simplejson.dumps(list(listElements)))
        logging.info('Tenemos ESTOS elementos:'+str(myTags.count())+"generamos"+salida)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(salida)    
        
    def getUserData(self):
        logging.info('______ getUserData ________')
        user= users.get_current_user()
        myUserData=UserData.gql("WHERE MyUser = :1",users.get_current_user())
        if myUserData.count()>0:
            userShowed=myUserData.get()
            logging.info('los datos ya estan creados')
        else :
            userShowed=UserData()
            userShowed.Mail=users.get_current_user().email()
            logging.info('creamos los datos')
        logging.info('El objeto en ddbb:'+userShowed.Mail)
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(userShowed.SaveToJSON())        
        