from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class ActionDataFilter(Serializable):
    fromStateData: str = None
    useResults: bool = None
    results: str = None
    toStateData: str = None

    def __init__(self,
                 fromStateData: str = None,
                 useResults: bool = None,
                 results: str = None,
                 toStateData: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
