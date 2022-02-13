from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.databased_switch_state_timeout import DataBasedSwitchStateTime0ut
from serverlessworkflow.sdk.default_condition_def import DefaultConditionDef
from serverlessworkflow.sdk.end_data_condition import EndDataCondition
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition_data_condition import TransitionDataCondition


class DataBasedSwitchState(State):
    id: str = None
    name: str = None
    type: str = None
    stateDataFilter: StateDataFilter = None
    timeouts: DataBasedSwitchStateTime0ut = None
    dataConditions: (TransitionDataCondition | EndDataCondition) = None
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
                 dataConditions: (TransitionDataCondition | EndDataCondition) = None,
                 onErrors: [Error] = None,
                 defaultCondition: DefaultConditionDef = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
