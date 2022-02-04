from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeout
from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeout


class Timeouts:
    workflowExecTimeout: WorkflowExecTimeout = None
    stateExecTimeout: StateExecTimeout = None
    actionExecTimeout: str = None  # ActionExecTimeout
    branchExecTimeout: str = None  # BranchExecTimeout
    eventTimeout: str = None  # EventTimeout

    def __init__(self,
                 workflowExecTimeout: WorkflowExecTimeout = None,
                 stateExecTimeout: StateExecTimeout = None,
                 actionExecTimeout: str = None,  # ActionExecTimeout
                 branchExecTimeout: str = None,  # BranchExecTimeout
                 eventTimeout: str = None,  # EventTimeout
                 **kwargs):

        # duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
