from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class CorrelationDef(Serializable):
    contextAttributeName: str = None
    contextAttributeValue: str = None

    def __init__(self,
                 contextAttributeName: str = None,
                 contextAttributeValue: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
