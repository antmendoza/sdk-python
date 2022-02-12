from typing import Union, Dict

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.inject_state_timeout import InjectStateTimeOut
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.transition import Transition


class InjectState(State):
    id: str = None
    name: str = None
    type: 'inject' = None
    end: Union[bool, End] = None
    data: Union[str, Dict[str, Dict]] = None
    timeouts: InjectStateTimeOut = None
    stateDataFilter: StateDataFilter = None
    transition: Union[str, Transition] = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: 'inject' = None,
                 end: Union[bool, End] = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 timeouts: InjectStateTimeOut = None,
                 stateDataFilter: StateDataFilter = None,
                 transition: Union[str, Transition] = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
