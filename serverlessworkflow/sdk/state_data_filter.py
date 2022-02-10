from serverlessworkflow.sdk.test import Attributes


class StateDataFilter:
    input: str = None
    output: str = None

    def __init__(self,
                 input: str = None,
                 output: str = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
