from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.metadata import Metadata


class BearerPropsDef:
    token: str = None
    metadata: Metadata = None

    def __init__(self,
                 token: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
