from serverlessworkflow.sdk.test import Attributes


class EventDataFilter:
    useData: bool = None
    data: str = None
    toStateData: str = None

    def __init__(self,
                 useData: bool = None,
                 data: str = None,
                 toStateData: str = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
