from __future__ import annotations

import copy

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.hydrate import HydratableParameter, UnionTypeOf, ComplexTypeOf, SimpleTypeOf
from serverlessworkflow.sdk.metadata import Metadata


class EndEventCondition:
    name: str = None
    eventRef: str = None
    end: (str | End) = None
    eventDataFilter: EventDataFilter = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 eventRef: str = None,
                 end: (str | End) = None,
                 eventDataFilter: EventDataFilter = None,
                 metadata: Metadata = None,
                 **kwargs):

        Fields(locals(), kwargs, EndEventCondition.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'end':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(End)]))

        if p_key == 'eventDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(EventDataFilter))

        return copy.deepcopy(p_value)
