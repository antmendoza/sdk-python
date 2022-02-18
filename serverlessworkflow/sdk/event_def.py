from __future__ import annotations

from enum import Enum

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.correlation_def import CorrelationDef
from serverlessworkflow.sdk.metadata import Metadata


class Kind(Enum):
    CONSUMED = "consumed"
    PRODUCED = "produced"


class EventDef:
    name: str = None
    source: str = None
    type: str = None
    kind: Kind = None
    correlation: (CorrelationDef | [CorrelationDef]) = None
    dataOnly: bool = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 source: str = None,
                 type: str = None,
                 kind: Kind = None,
                 correlation: (CorrelationDef | [CorrelationDef]) = None,  # CorrelationDefs
                 dataOnly: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
