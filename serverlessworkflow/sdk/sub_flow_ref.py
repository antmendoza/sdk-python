from enum import Enum

from serverlessworkflow.sdk.enums import Invoke
from serverlessworkflow.sdk.test import Attributes


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

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
