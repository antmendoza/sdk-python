from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.metadata import Metadata


class BasicPropsDef:
    username: str = None
    password: str = None
    metadata: Metadata = None

    def __init__(self,
                 username: str = None,
                 password: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
