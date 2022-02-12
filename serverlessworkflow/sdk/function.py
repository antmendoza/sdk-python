from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.class_properties import ClassProperties


class FunctionType:
    REST = "rest"
    ASYNCAPI = "asyncapi"
    RPC = "rpc"
    GRAPHQL = "graphql"
    ODATA = "odata"
    EXPRESSION = "expression"
    CUSTOM = "custom"


class Function:
    name: str = None
    operation: str = None
    type: FunctionType = None
    authRef: str = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 operation: str = None,
                 type: FunctionType = None,
                 authRef: str = None,
                 metadata: Metadata = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
