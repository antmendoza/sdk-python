from serverlessworkflow.sdk.class_properties import Properties


class EventDataFilter:
    useData: bool = None
    data: str = None
    toStateData: str = None

    def __init__(self,
                 useData: bool = None,
                 data: str = None,
                 toStateData: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
