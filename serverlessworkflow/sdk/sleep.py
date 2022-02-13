from serverlessworkflow.sdk.class_properties import Properties


class Sleep:
    before: str = None
    after: str = None

    def __init__(self,
                 before: str = None,
                 after: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
