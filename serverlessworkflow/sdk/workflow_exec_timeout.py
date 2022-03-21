from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class WorkflowExecTimeOut(Serializable):
    duration: str = None
    interrupt: bool = None
    runBefore: str = None

    def __init__(self,
                 duration: str = None,
                 interrupt: bool = None,
                 runBefore: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
