from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class BranchTimeOut(Serializable):
    actionExecTimeOut: str = None  # ActionExecTimeOut
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 actionExecTimeOut: str = None,
                 branchExecTimeOut: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
