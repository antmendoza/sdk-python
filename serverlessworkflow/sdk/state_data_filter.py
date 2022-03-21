from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class StateDataFilter(Serializable):
    input: str = None
    output: str = None

    def __init__(self,
                 input: str = None,
                 output: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
