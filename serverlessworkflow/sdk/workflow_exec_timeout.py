from serverlessworkflow.sdk.class_properties import Properties


class WorkflowExecTimeOut:
    duration: str = None
    interrupt: bool = None
    runBefore: str = None

    def __init__(self,
                 duration: str = None,
                 interrupt: bool = None,
                 runBefore: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
