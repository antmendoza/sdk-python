from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.inject_state_timeout import InjectStateTimeOut
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class InjectState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (str | End) = None
    data: (str | Dict[str, Dict]) = None
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
                 end: (str | End) = None,
                 data: (str | Dict[str, Dict]) = None,
                 timeouts: InjectStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
