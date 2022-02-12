from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.class_properties import ClassProperties


class BasicPropsDef:
    username: str = None
    password: str = None
    metadata: Metadata = None

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 metadata: Metadata = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
