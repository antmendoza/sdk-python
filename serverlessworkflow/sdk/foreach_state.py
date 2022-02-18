from __future__ import annotations

from enum import Enum

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.foreach_state_timeout import ForEachStateTimeOut
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class ForEachStateMode(Enum):
    PARALLEL = "parallel"
    SEQUENTIAL = "sequential"


class ForEachState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (str | End) = None
    inputCollection: str = None
    outputCollection: str = None
    iterationParam: str = None
    batchSize: (int | str) = None
    actions: [Action] = None
    timeouts: ForEachStateTimeOut = None
    stateDataFilter: StateDataFilter = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    mode: ForEachStateMode = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 end: (str | End) = None,
                 inputCollection: str = None,
                 outputCollection: str = None,
                 iterationParam: str = None,
                 batchSize: (int | str) = None,
                 actions: [Action] = None,
                 timeouts: ForEachStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 mode: ForEachStateMode = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, ForEachState.load_properties).set_to_object(self)

    @staticmethod
    def load_properties(local, value):
        if local == 'actions':
            value = ForEachState.load_actions(value)
        return value

    @staticmethod
    def load_actions(actions):
        return [Action(**action) if type(action) is not Action else action for action in actions]
