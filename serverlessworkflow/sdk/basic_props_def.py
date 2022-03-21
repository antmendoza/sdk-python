from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable


class BasicPropsDef(Serializable):
    username: str = None
    password: str = None
    metadata: Metadata = None

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
