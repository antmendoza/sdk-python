from serverlessworkflow.sdk.test import Attributes


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

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
