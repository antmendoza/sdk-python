class Callbackstate:
     id= None
     name= None
     type= None
     action= None
     eventRef= None
     timeouts= None
     stateExecTimeout= None
     actionExecTimeout= None
     eventTimeout= None
     eventDataFilter= None
     stateDataFilter= None
     onErrors= None
     transition= None
     end= None
     compensatedBy= None
     usedForCompensation= None
     metadata= None
     def __init__(self, 
         id= None,
         name= None,
         type= None,
         action= None,
         eventRef= None,
         timeouts= None,
         stateExecTimeout= None,
         actionExecTimeout= None,
         eventTimeout= None,
         eventDataFilter= None,
         stateDataFilter= None,
         onErrors= None,
         transition= None,
         end= None,
         compensatedBy= None,
         usedForCompensation= None,
         metadata= None,
         **kwargs):
 
# duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated


            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
