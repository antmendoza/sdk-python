from serverlessworkflow.sdk.test import Attributes


class State:
    type: str

    def __init__(self, data: dict = None,
                 **kwargs):
        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
