from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class Sleep(Serializable):
    before: str = None
    after: str = None

    def __init__(self,
                 before: str = None,
                 after: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
