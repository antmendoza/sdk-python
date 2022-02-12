from serverlessworkflow.sdk.class_properties import ClassProperties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class ParallelStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 branchExecTimeOut: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
