from serverlessworkflow.sdk.class_properties import Properties


class StateDataFilter:
    input: str = None
    output: str = None

    def __init__(self,
                 input: str = None,
                 output: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
