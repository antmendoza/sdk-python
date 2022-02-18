from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeOut


class ContinueAsDef:
    workflowId: str = None
    version: str = None
    data: (str | Dict[str, Dict]) = None
    workflowExecTimeOut: WorkflowExecTimeOut = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 data: (str | Dict[str, Dict]) = None,
                 workflowExecTimeOut: WorkflowExecTimeOut = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
