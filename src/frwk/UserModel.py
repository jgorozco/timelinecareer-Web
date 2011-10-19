from frwk.JSONUtils import JSONUtils
from google.appengine.ext import db
import simplejson
import logging
import copy


class ModelDTO(simplejson.JSONEncoder):
    MyModelo=dict()
    TYPES = {} 
    def __init__(self,objeto=0):
        if objeto!=0 :
            diccionario=simplejson.loads(objeto)
            self.__dict__=diccionario
            self=JSONUtils.dict2obj(simplejson.loads(objeto))

    def default(self, obj):
        if isinstance(obj, self.TYPES.values()):
            key = '__%s__' % obj.__class__.__name__
            return { key: obj.__dict__ }
        return simplejson.JSONEncoder.default(self, obj)

    def Serialize(self):
        return simplejson.dumps(self.__dict__)

    def CustomTypeDecoder(self,dct):
        if len(dct) == 1:
            type_name, value = dct.items()[0]
            type_name = type_name.strip('_')
            if type_name in self.TYPES:
                return self.TYPES[type_name].from_dict(value)
        return dct
    
    def LoadFromJSON(self,objetoJSON):
         pass
    
    def SaveToJSON(self):
        pass

class ListDTO(db.GqlQuery):
    
     listSerializable=[]
     
     def __init__(self,listado=[]):
     #generamos un array con solo los diccionarios
        mylistSerializable=list()
        for element in listado:
            elemento=element
            elemento.SaveToJSON()
            mylistSerializable.append(copy.copy(elemento.MyModelo.__dict__))
        self.listSerializable=mylistSerializable
     def Serialize(self):
        return simplejson.dumps(self.listSerializable) 
        
         
     #lo dumpeamos for free

class CompleteData():
    userData=ModelDTO()
    theme=ModelDTO()
    tags=ListDTO()
    proyects=ListDTO() 
    
    def __init__(self,userData,theme,tags,proyects):
        self.userData=userData
        self.theme=theme
        self.tags=tags
        self.proyects=proyects
        
    def SaveToJSON(self):
            self.userData.SaveToJSON()
            self.theme.SaveToJSON()
            objetoSalida={'Data':{
                                  'UserData':self.userData.MyModelo.__dict__ ,
                                  'Theme':self.theme.MyModelo.__dict__ ,
                                  'Tags':self.tags.listSerializable ,
                                  'Proyects':self.proyects.listSerializable
                                  }
                           }
            return  simplejson.dumps(objetoSalida)

class UserData(db.Model):
    MyUser= db.UserProperty()
    Name = db.StringProperty()
    Phone = db.StringProperty()
    Address =db.StringProperty()
    University=db.StringProperty()
    DriveLicense=db.StringProperty()
    Poblation=db.StringProperty()
    Nationality=db.StringProperty()
    Mail=db.StringProperty()
    Photo=db.StringProperty()
    initialDate=db.StringProperty()
    MyModelo=ModelDTO()
   
    
# esta funcion es una puta mierda, deberia ser algo automatico o algo asi, pero llevo 2 dias
# y no he conseguido sacarlo, no se como hostias hacer que extienda de model y de jsonEncoder asi que a lo burro.
#    
    def LoadFromJSON(self,objetoJSON):
        MyModelo=ModelDTO(objetoJSON)
        self.Name=MyModelo.Name
        self.Phone=MyModelo.Phone
        self.Address=MyModelo.Address
        self.University=MyModelo.University
        self.DriveLicense=MyModelo.DriveLicense
        self.Poblation=MyModelo.Poblation
        self.Nationality=MyModelo.Nationality
        self.Mail=MyModelo.Mail
        self.Photo=MyModelo.Photo
        self.initialDate=MyModelo.initialDate
        
    def SaveToJSON(self):
        self.MyModelo.Name=self.Name
        self.MyModelo.Phone=self.Phone
        self.MyModelo.Address=self.Address
        self.MyModelo.University=self.University
        self.MyModelo.DriveLicense=self.DriveLicense
        self.MyModelo.Poblation=self.Poblation
        self.MyModelo.Nationality=self.Nationality
        self.MyModelo.Mail=self.Mail
        self.MyModelo.Photo=self.Photo
        self.MyModelo.initialDate=self.initialDate
        try:#si falla es que lo acabas de crear
            self.MyModelo.id=str(self.key().id())
        except :
            pass
        return self.MyModelo.Serialize()
      
       
###############################################################################################
#######                                                                            ############
#######                                                                            ############
#######                                                                            ############    
###############################################################################################  
  
class Proyect(db.Model):
    MyUser = db.UserProperty()   
    Profesional=db.StringProperty()
    Name=db.StringProperty()
    Category=db.StringProperty()
    SubCategory=db.StringProperty()
    InitDate=db.StringProperty()
    EndDate=db.StringProperty()
    Description=db.TextProperty()
    Company=db.StringProperty()
    Url=db.StringProperty()
    MyModelo=ModelDTO()
 
# Una mierda de nuevo
#
# 
    
    def LoadFromJSON(self,objetoJSON):
        MyModelo=ModelDTO(objetoJSON)
        self.Name=MyModelo.Name
        self.Profesional=MyModelo.Profesional
        self.Category=MyModelo.Category
        self.SubCategory=MyModelo.SubCategory
        self.InitDate=MyModelo.InitDate
        self.EndDate=MyModelo.EndDate
        self.Description=MyModelo.Description
        self.Company=MyModelo.Company
        self.Url=MyModelo.Url

        
    def SaveToJSON(self):
        self.MyModelo.Name=self.Name
        self.MyModelo.Profesional=self.Profesional
        self.MyModelo.Category=self.Category
        self.MyModelo.SubCategory=self.SubCategory
        self.MyModelo.InitDate=self.InitDate
        self.MyModelo.EndDate=self.EndDate
        self.MyModelo.Description=self.Description
        self.MyModelo.Company=self.Company
        self.MyModelo.Url=self.Url
        self.MyModelo.id=self.key().id()
        return self.MyModelo.Serialize()
    
    
###############################################################################################
#######                                                                            ############
#######                                                                            ############
#######                                                                            ############    
############################################################################################### 
 
class Tags(db.Model):
    MyUser= db.UserProperty()
    Name=db.StringProperty()
    Color=db.StringProperty()
    MyModelo=ModelDTO()
# Una mierda one more time
#
# 
    
    def LoadFromJSON(self,objetoJSON):
        MyModelo=ModelDTO(objetoJSON)
        self.Name=MyModelo.Name
        self.Color=MyModelo.Color

        
    def SaveToJSON(self):
        self.MyModelo.Name=self.Name
        self.MyModelo.Color=self.Color
        self.MyModelo.id=self.key().id()        
        return self.MyModelo.Serialize()
 
 
###############################################################################################
#######                                                                            ############
#######                                                                            ############
#######                                                                            ############    
############################################################################################### 
    
    
class Category(db.Model):
    MyUser= db.UserProperty()
    Name=db.StringProperty()
    Color=db.StringProperty()
    IsSub=db.StringProperty()
    MyModelo=ModelDTO()
# Una mierda one more time
#
# 
    
    def LoadFromJSON(self,objetoJSON):
        MyModelo=ModelDTO(objetoJSON)
        self.Name=MyModelo.Name
        self.IsSub=MyModelo.IsSub
        self.Color=MyModelo.Color

        
    def SaveToJSON(self):
        self.MyModelo.Name=self.Name
        self.MyModelo.IsSub=self.IsSub
        self.MyModelo.Color=self.Color
        self.MyModelo.id=self.key().id()
        return self.MyModelo.Serialize()   
    
    
    
###############################################################################################
#######                                                                            ############
#######                                                                            ############
#######                                                                            ############    
###############################################################################################
    
class Theme(db.Model):
    MyUser =db.UserProperty()
    line_scuare_1=db.StringProperty()
    line_content_1=db.StringProperty()
    line_scuare_2=db.StringProperty()
    line_content_2=db.StringProperty()
    bg_application=db.StringProperty()
    bg_timeline=db.StringProperty()
    line_timeline=db.StringProperty()
    bg_personal_data=db.StringProperty()
    bg_personal_line=db.StringProperty()
    close_button=db.StringProperty()
    line_bg_proyect_sheet=db.StringProperty()
    bg_proyectlist=db.StringProperty()
    bg_proyect_sheet=db.StringProperty()
    line_bg_proyect_sheet_personal=db.StringProperty()
    bg_proyect_sheet_personal=db.StringProperty()
    soft_sep=db.StringProperty()
    hard_sep=db.StringProperty()
    cursor_timeline=db.StringProperty()
    bg_proyectsheet_details=db.StringProperty()
    scrollbar_proyectsheet_details=db.StringProperty()
    MyModelo=ModelDTO()
# Una mierda one more time
#
# 
    
    def LoadFromJSON(self,objetoJSON):
        MyModelo=ModelDTO(objetoJSON)
        self.line_timeline=MyModelo.line_timeline
        self.line_scuare_1=MyModelo.line_scuare_1
        self.line_content_1=MyModelo.line_content_1
        self.line_scuare_2=MyModelo.line_scuare_2
        self.line_content_2=MyModelo.line_content_2
        self.bg_application=MyModelo.bg_application
        self.bg_timeline=MyModelo.bg_timeline
        self.bg_proyectlist=MyModelo.bg_proyectlist
        self.bg_personal_data=MyModelo.bg_personal_data
        self.close_button=MyModelo.close_button
        self.line_bg_proyect_sheet=MyModelo.line_bg_proyect_sheet
        self.bg_personal_data=MyModelo.bg_personal_data
        self.bg_personal_line=MyModelo.bg_personal_line
        self.close_button=MyModelo.close_button
        self.line_bg_proyect_sheet=MyModelo.line_bg_proyect_sheet
        self.bg_proyect_sheet=MyModelo.bg_proyect_sheet
        self.line_bg_proyect_sheet_personal=MyModelo.line_bg_proyect_sheet_personal
        self.bg_proyect_sheet_personal=MyModelo.bg_proyect_sheet_personal
        self.soft_sep=MyModelo.soft_sep
        self.hard_sep=MyModelo.hard_sep
        self.cursor_timeline=MyModelo.cursor_timeline
        self.bg_proyectsheet_details=MyModelo.bg_proyectsheet_details
        self.scrollbar_proyectsheet_details=MyModelo.scrollbar_proyectsheet_details
        
    def SaveToJSON(self):
        self.MyModelo.line_timeline=self.line_timeline
        self.MyModelo.line_scuare_1=self.line_scuare_1
        self.MyModelo.line_content_1=self.line_content_1
        self.MyModelo.line_scuare_2=self.line_scuare_2
        self.MyModelo.line_content_2=self.line_content_2
        self.MyModelo.bg_application=self.bg_application
        self.MyModelo.bg_proyectlist=self.bg_proyectlist
        self.MyModelo.bg_timeline=self.bg_timeline
        self.MyModelo.bg_personal_data=self.bg_personal_data
        self.MyModelo.close_button=self.close_button
        self.MyModelo.line_bg_proyect_sheet=self.line_bg_proyect_sheet
        self.MyModelo.bg_personal_data=self.bg_personal_data
        self.MyModelo.bg_personal_line=self.bg_personal_line
        self.MyModelo.close_button=self.close_button
        self.MyModelo.line_bg_proyect_sheet=self.line_bg_proyect_sheet
        self.MyModelo.bg_proyect_sheet=self.bg_proyect_sheet
        self.MyModelo.line_bg_proyect_sheet_personal=self.line_bg_proyect_sheet_personal
        self.MyModelo.bg_proyect_sheet_personal=self.bg_proyect_sheet_personal
        self.MyModelo.soft_sep=self.soft_sep
        self.MyModelo.hard_sep=self.hard_sep
        self.MyModelo.cursor_timeline=self.cursor_timeline
        self.MyModelo.bg_proyectsheet_details=self.bg_proyectsheet_details
        self.MyModelo.scrollbar_proyectsheet_details=self.scrollbar_proyectsheet_details
#        self.MyModelo.id=self.key().id()        
        return self.MyModelo.Serialize()

