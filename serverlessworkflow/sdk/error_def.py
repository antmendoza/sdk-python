from serverlessworkflow.sdk.class_properties import Properties


class ErrorDef:
    name: str = None
    code: str = None
    description: str = None

    def __init__(self,
                 name: str = None,
                 code: str = None,
                 description: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
