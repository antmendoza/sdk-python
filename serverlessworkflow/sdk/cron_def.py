from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class CronDef(Serializable):
    expression: str = None
    validUntil: str = None

    def __init__(self,
                 expression: str = None,
                 validUntil: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
