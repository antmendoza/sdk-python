from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.metadata import Metadata


class BearerPropsDef:
    token: str = None
    metadata: Metadata = None

    def __init__(self,
                 token: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
