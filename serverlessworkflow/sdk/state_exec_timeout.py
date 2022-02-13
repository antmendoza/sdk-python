from serverlessworkflow.sdk.class_properties import Properties


class StateExecTimeOut:
    single: str = None
    total: str = None

    def __init__(self,
                 single: str = None,
                 total: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
