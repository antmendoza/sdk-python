from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut
from serverlessworkflow.sdk.test import Attributes
from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeOut


class WorkflowTimeOut:
    workflowExecTimeOut: WorkflowExecTimeOut = None
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    branchExecTimeOut: str = None  # BranchExecTimeOut
    eventTimeOut: str = None  # EventTimeOut

    def __init__(self,
                 workflowExecTimeOut: WorkflowExecTimeOut = None,
                 stateExecTimeOut: StateExecTimeOut = None,
                 actionExecTimeOut: str = None,  # ActionExecTimeOut
                 branchExecTimeOut: str = None,  # BranchExecTimeOut
                 eventTimeOut: str = None,  # EventTimeOut
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
