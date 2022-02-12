from enum import Enum

from serverlessworkflow.sdk.enums import Invoke
from serverlessworkflow.sdk.class_properties import ClassProperties


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

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
