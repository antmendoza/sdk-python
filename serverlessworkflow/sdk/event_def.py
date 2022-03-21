from __future__ import annotations

import copy
from enum import Enum

from serverlessworkflow.sdk.correlation_def import CorrelationDef
from serverlessworkflow.sdk.hydration import HydratableParameter, UnionTypeOf, ArrayTypeOf, ComplexTypeOf, \
    Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable


class Kind(Enum):
    CONSUMED = "consumed"
    PRODUCED = "produced"


class EventDef(Serializable):
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
        Serializable.__init__(self)
        Fields(locals(), kwargs, EventDef.f_hydration,
               {'kind': 'consumed', 'dataOnly': True, }).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'correlation':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([ComplexTypeOf(CorrelationDef),
                                                                             ArrayTypeOf(CorrelationDef)]))
        return copy.deepcopy(p_value)
