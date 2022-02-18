from __future__ import annotations

from serverlessworkflow.sdk.branch import Branch
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.tobedone.parallel_state_timeout import ParallelStateTimeOut
from serverlessworkflow.sdk.tobedone.state import State
from serverlessworkflow.sdk.tobedone.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.tobedone.transition import Transition


class ParallelState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (bool | End) = None
    stateDataFilter: StateDataFilter = None
    timeouts: ParallelStateTimeOut = None
    branches: [Branch] = None
    completionType: str = None
    numCompleted: (int | str) = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 end: (bool | End) = None,
                 stateDataFilter: StateDataFilter = None,
                 timeouts: ParallelStateTimeOut = None,
                 branches: [Branch] = None,
                 completionType: str = None,
                 numCompleted: (int | str) = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)



