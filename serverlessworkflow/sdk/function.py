from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.test import Attributes


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

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
