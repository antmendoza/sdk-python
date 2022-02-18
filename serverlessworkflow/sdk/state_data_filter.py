from serverlessworkflow.sdk.class_properties import Fields


class StateDataFilter:
    input: str = None
    output: str = None

    def __init__(self,
                 input: str = None,
                 output: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
