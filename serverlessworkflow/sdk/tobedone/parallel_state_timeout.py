from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.state_exec_timeout import StateExecTimeOut


class ParallelStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 branchExecTimeOut: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
