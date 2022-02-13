from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.sleep_state_timeout import SleepStateTimeOut
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class SleepState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (str | End) = None
    stateDataFilter: StateDataFilter = None
    duration: str = None
    timeouts: SleepStateTimeOut = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 end: (str | End) = None,
                 stateDataFilter: StateDataFilter = None,
                 duration: str = None,
                 timeouts: SleepStateTimeOut = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
