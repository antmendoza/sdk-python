from serverlessworkflow.sdk.class_properties import Properties


class ActionDataFilter:
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
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
