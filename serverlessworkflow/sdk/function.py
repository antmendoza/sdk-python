from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable


class Function(Serializable):
    name: str = None
    operation: str = None
    type: str = None
    authRef: str = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 operation: str = None,
                 type: str = None,
                 authRef: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Serializable.__init__(self)

        Fields(locals(), kwargs, Fields.default_hydration,
               {'type': 'rest'}).set_to_object(self)
