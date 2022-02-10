from enum import Enum
from typing import Union, List

from serverlessworkflow.sdk.correlation_def import CorrelationDef
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.test import Attributes


class Kind(Enum):
    CONSUMED = "consumed"
    PRODUCED = "produced"


class EventDef:
    name: str = None
    source: str = None
    type: str = None
    kind: Kind = None
    correlation: Union[CorrelationDef, List[CorrelationDef]] = None
    dataOnly: bool = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 source: str = None,
                 type: str = None,
                 kind: Kind = None,
                 correlation: Union[CorrelationDef, List[CorrelationDef]] = None,  # CorrelationDefs
                 dataOnly: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
