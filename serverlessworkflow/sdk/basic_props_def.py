from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.attributes import Attributes


class BasicPropsDef:
    username: str = None
    password: str = None
    metadata: Metadata = None

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
