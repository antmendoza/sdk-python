from serverlessworkflow.sdk.class_properties import ClassProperties


class WorkflowExecTimeOut:
    duration: str = None
    interrupt: bool = None
    runBefore: str = None

    def __init__(self,
                 duration: str = None,
                 interrupt: bool = None,
                 runBefore: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
