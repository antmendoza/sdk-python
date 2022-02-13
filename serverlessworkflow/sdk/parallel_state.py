from __future__ import annotations

from enum import Enum

from serverlessworkflow.sdk.branch import Branch
from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.parallel_state_timeout import ParallelStateTimeOut
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class ParallelStateCompletionType(Enum):
    allOf = "allOf"
    atLeast = "atLeast"


class ParallelState(State):
    id: str = None
    name: str = None
    type: str = None
    end: (str | End) = None
    stateDataFilter: StateDataFilter = None
    timeouts: ParallelStateTimeOut = None
    branches: [Branch] = None
    completionType: ParallelStateCompletionType = None
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
                 end: (str | End) = None,
                 stateDataFilter: StateDataFilter = None,
                 timeouts: ParallelStateTimeOut = None,
                 branches: [Branch] = None,
                 completionType: ParallelStateCompletionType = None,
                 numCompleted: (int | str) = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
