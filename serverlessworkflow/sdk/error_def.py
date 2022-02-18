from serverlessworkflow.sdk.class_properties import Fields


class ErrorDef:
    name: str = None
    code: str = None
    description: str = None

    def __init__(self,
                 name: str = None,
                 code: str = None,
                 description: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
