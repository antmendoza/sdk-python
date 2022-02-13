from __future__ import annotations

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.callback_state_timeout import CallbackStateTimeOut
from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class CallbackState(State):
    id: str = None
    name: str = None
    type: 'callback' = None
    action: Action = None
    eventRef: str = None
    timeouts: CallbackStateTimeOut = None
    eventDataFilter: EventDataFilter = None
    stateDataFilter: StateDataFilter = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    end: (str | End) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: 'callback' = None,
                 action: Action = None,
                 eventRef: str = None,
                 timeouts: CallbackStateTimeOut = None,
                 eventDataFilter: EventDataFilter = None,
                 stateDataFilter: StateDataFilter = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 end: (str | End) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
