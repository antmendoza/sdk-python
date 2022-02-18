from __future__ import annotations

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.operation_state_timeout import OperationStateTimeOut
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class OperationState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (str | End) = None
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
                 end: (str | End) = None,
                 **kwargs):
        Fields(locals(), kwargs, OperationState.load_properties).set_to_object(self)

    @staticmethod
    def load_properties(k, value):
        if k == 'actions':
            value = OperationState.load_actions(value)
        return value

    @staticmethod
    def load_actions(actions):
        return [Action(**action) if type(action) is not Action else action for action in actions]
