class Produceeventdef:
     eventRef= None
     data= None
     contextAttributes= None
     def __init__(self, 
         eventRef= None,
         data= None,
         contextAttributes= None,
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
