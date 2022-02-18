from enum import Enum

from serverlessworkflow.sdk.class_properties import Fields
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
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
