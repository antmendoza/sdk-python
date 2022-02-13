from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.event_state_timeout import EventStateTimeOut
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.on_events import OnEvents
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class EventState(State):
    id: str = None
    name: str = None
    type: str = None
    exclusive: bool = None
    onEvents: [OnEvents] = None
    timeouts: EventStateTimeOut = None
    stateDataFilter: StateDataFilter = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    end: (str | End) = None
    compensatedBy: str = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 exclusive: bool = None,
                 onEvents: [OnEvents] = None,
                 timeouts: EventStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 end: (str | End) = None,
                 compensatedBy: str = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
