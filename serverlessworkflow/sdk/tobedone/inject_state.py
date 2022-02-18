from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
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
    data: (str | Dict) = None
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
                 data: (str | Dict) = None,
                 timeouts: InjectStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
