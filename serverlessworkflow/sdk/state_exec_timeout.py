from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class StateExecTimeOut(Serializable):
    single: str = None
    total: str = None

    def __init__(self,
                 single: str = None,
                 total: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
