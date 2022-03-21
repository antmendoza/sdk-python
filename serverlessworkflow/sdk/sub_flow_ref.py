from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class SubFlowRef(Serializable):
    workflowId: str = None
    version: str = None
    onParentComplete: str = None
    invoke: str = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 onParentComplete: str = None,
                 invoke: str = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
