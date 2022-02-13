from enum import Enum

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.enums import Invoke


class SubFlowRefOnParentComplete(Enum):
    CONTINUE = "continue"
    TERMINATE = "terminate"


class SubFlowRef:
    workflowId: str = None
    version: str = None
    onParentComplete = None
    invoke: Invoke = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 onParentComplete=None,
                 invoke: Invoke = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
