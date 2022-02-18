from __future__ import annotations

import copy

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, UnionTypeOf, SimpleTypeOf, ComplexTypeOf
from serverlessworkflow.sdk.tobedone.inject_state_timeout import InjectStateTimeOut
from serverlessworkflow.sdk.tobedone.metadata import Metadata
from serverlessworkflow.sdk.tobedone.state import State
from serverlessworkflow.sdk.tobedone.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.tobedone.transition import Transition


class InjectState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (bool | End) = None
    data: (str | dict) = None
    timeouts: InjectStateTimeOut = None
    stateDataFilter: StateDataFilter = None
    transition: (str | Transition) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 end: (bool | End) = None,
                 data: (str | dict) = None,
                 timeouts: InjectStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, InjectState.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'end':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf(SimpleTypeOf(bool),
                                                                            ComplexTypeOf(End)))
        if p_key == 'data':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(dict)]))
        if p_key == 'timeouts':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(InjectStateTimeOut))

        if p_key == 'stateDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(StateDataFilter))

        if p_key == 'transition':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(Transition)]))

        return copy.deepcopy(p_value)
