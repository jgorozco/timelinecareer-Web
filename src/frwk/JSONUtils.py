import simplejson
class JSONUtils(object):





    @staticmethod
    def dict2obj(d):
            if isinstance(d, dict):
                n = {}
                for item in d:
                    if isinstance(d[item], dict):
                        n[item] = self.dict2obj(d[item])
                    elif isinstance(d[item], (list, tuple)):
                        n[item] = [self.dict2obj(elem) for elem in d[item]]
                    else:
                        n[item] = d[item]
                return type('obj_from_dict', (object,), n)
            else:
                return d
   
    @staticmethod        
    def json_repr(obj):
      def serialize(obj):
        """Recursively walk object's hierarchy."""
        if isinstance(obj, (bool, int, long, float, basestring)):
          return obj
        elif isinstance(obj, dict):
          obj = obj.copy()
          for key in obj:
            obj[key] = serialize(obj[key])
          return obj
        elif isinstance(obj, list):
          return [serialize(item) for item in obj]
        elif isinstance(obj, tuple):
          return tuple(serialize([item for item in obj]))
        elif hasattr(obj, '__dict__'):
          return serialize(obj.__dict__)
        else:
          return repr(obj) # Don't know how to handle, convert to string
      return simplejson.dumps(serialize(obj))            
  