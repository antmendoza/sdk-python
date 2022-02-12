from serverlessworkflow.sdk.class_properties import ClassProperties


class StateExecTimeOut:
    single: str = None
    total: str = None

    def __init__(self,
                 single: str = None,
                 total: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
