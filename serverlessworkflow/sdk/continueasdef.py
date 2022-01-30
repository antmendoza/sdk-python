from typing import Union, Dict

from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeout


class Continueasdef:
    workflowId: str = None
    version: str = None
    data: Union[str, Dict[str, Dict]] = None
    workflowExecTimeout: WorkflowExecTimeout = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 workflowExecTimeout: WorkflowExecTimeout = None,
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
