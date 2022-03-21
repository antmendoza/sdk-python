from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class ErrorDef(Serializable):
    name: str = None
    code: str = None
    description: str = None

    def __init__(self,
                 name: str = None,
                 code: str = None,
                 description: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
