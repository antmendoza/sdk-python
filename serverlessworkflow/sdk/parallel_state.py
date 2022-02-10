from enum import Enum
from typing import Union

from serverlessworkflow.sdk.branch import Branch
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.parallel_state_timeout import ParallelStateTimeOut
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.test import Attributes
from serverlessworkflow.sdk.transition import Transition


class ParallelStateCompletionType(Enum):
    allOf = "allOf"
    atLeast = "atLeast"


class ParallelState:
    id: str = None
    name: str = None
    type: str = None
    end: Union[bool, End] = None
    stateDataFilter: StateDataFilter = None
    timeouts: ParallelStateTimeOut = None
    branches: [Branch] = None
    completionType: ParallelStateCompletionType = None
    numCompleted: Union[int, str] = None
    onErrors: [Error] = None
    transition: Union[str, Transition] = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 end: Union[bool, End] = None,
                 stateDataFilter: StateDataFilter = None,
                 timeouts: ParallelStateTimeOut = None,
                 branches: [Branch] = None,
                 completionType: ParallelStateCompletionType = None,
                 numCompleted: Union[int, str] = None,
                 onErrors: [Error] = None,
                 transition: Union[str, Transition] = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
