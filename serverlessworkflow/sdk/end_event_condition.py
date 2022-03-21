from __future__ import annotations

import copy

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.hydration import HydratableParameter, UnionTypeOf, ComplexTypeOf, SimpleTypeOf, \
    Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable


class EndEventCondition(Serializable):
    name: str = None
    eventRef: str = None
    end: (bool | End) = None
    eventDataFilter: EventDataFilter = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 eventRef: str = None,
                 end: (bool | End) = None,
                 eventDataFilter: EventDataFilter = None,
                 metadata: Metadata = None,
                 **kwargs):

        Serializable.__init__(self)
        Fields(locals(), kwargs, EndEventCondition.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'end':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(bool),
                                                                             ComplexTypeOf(End)]))

        if p_key == 'eventDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(EventDataFilter))

        return copy.deepcopy(p_value)
