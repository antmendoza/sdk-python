from __future__ import annotations

import copy

from serverlessworkflow.sdk.databased_switch_state_timeout import DataBasedSwitchStateTime0ut
from serverlessworkflow.sdk.default_condition_def import DefaultConditionDef
from serverlessworkflow.sdk.end_data_condition import EndDataCondition
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.hydration import HydratableParameter, ComplexTypeOf, ArrayTypeOf, \
    Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition_data_condition import TransitionDataCondition


class DataBasedSwitchState(State, Serializable):
    id: str = None
    name: str = None
    type: str = None
    stateDataFilter: StateDataFilter = None
    timeouts: DataBasedSwitchStateTime0ut = None
    dataConditions: ([TransitionDataCondition] | [EndDataCondition]) = None
    onErrors: [Error] = None
    defaultCondition: DefaultConditionDef = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 stateDataFilter: StateDataFilter = None,
                 timeouts: DataBasedSwitchStateTime0ut = None,
                 dataConditions: ([TransitionDataCondition] | [EndDataCondition]) = None,
                 onErrors: [Error] = None,
                 defaultCondition: DefaultConditionDef = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        Serializable.__init__(self)
        Fields(locals(), kwargs, DataBasedSwitchState.f_hydration,
               {'type': 'switch', 'usedForCompensation': False}).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'stateDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(StateDataFilter))

        if p_key == 'timeouts':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(DataBasedSwitchStateTime0ut))

        if p_key == 'dataConditions':
            return [DataBasedSwitchState.hydrate_state(v) if not (
                isinstance(v, TransitionDataCondition or EndDataCondition)) else v for v in p_value]

        if p_key == 'onErrors':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Error))

        if p_key == 'defaultCondition':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(DefaultConditionDef))

        return copy.deepcopy(p_value)

    @staticmethod
    def hydrate_state(v):

        state = State(**v)
        if hasattr(state, "transition"):
            return TransitionDataCondition(**v)
        if hasattr(state, "end"):
            return EndDataCondition(**v)
        raise Exception(f"Unexpected DataBasedSwitchState value: {v}")
