from __future__ import annotations

import copy

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, ComplexTypeOf, ArrayTypeOf, UnionTypeOf, \
    SimpleTypeOf
from serverlessworkflow.sdk.operation_state_timeout import OperationStateTimeOut
from serverlessworkflow.sdk.tobedone.state import State
from serverlessworkflow.sdk.tobedone.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.tobedone.transition import Transition


class OperationState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (bool | End) = None
    stateDataFilter: StateDataFilter = None
    actionMode: str = None
    actions: [Action] = None
    timeouts: OperationStateTimeOut = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 stateDataFilter: StateDataFilter = None,
                 actionMode: str = None,
                 actions: [Action] = None,
                 timeouts: OperationStateTimeOut = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 end: (bool | End) = None,
                 **kwargs):
        Fields(locals(), kwargs, OperationState.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'stateDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(StateDataFilter))

        if p_key == 'actions':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Action))

        if p_key == 'timeouts':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(OperationStateTimeOut))

        if p_key == 'onErrors':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Error))

        if p_key == 'transition':
            return HydratableParameter(value=p_value).hydrateAs(
                UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(Transition)]))

        if p_key == 'end':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(bool), ComplexTypeOf(End)]))

        return copy.deepcopy(p_value)
