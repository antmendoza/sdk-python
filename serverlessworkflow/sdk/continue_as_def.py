from typing import Union, Dict

from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeOut


class ContinueAsDef:
    workflowId: str = None
    version: str = None
    data: Union[str, Dict[str, Dict]] = None
    workflowExecTimeOut: WorkflowExecTimeOut = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 workflowExecTimeOut: WorkflowExecTimeOut = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
