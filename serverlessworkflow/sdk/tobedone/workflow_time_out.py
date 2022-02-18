from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.state_exec_timeout import StateExecTimeOut
from serverlessworkflow.sdk.tobedone.workflow_exec_timeout import WorkflowExecTimeOut


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
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
