from typing import Union, Dict

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeout
from serverlessworkflow.sdk.statedatafilter import Statedatafilter
from serverlessworkflow.sdk.transition import Transition


class InjectStateTimeouts:
    stateExecTimeout: StateExecTimeout = None
    stateDataFilter: Statedatafilter = None


class Injectstate:
    id: str = None
    name: str = None
    type: 'inject' = None
    end: Union[bool, End] = None
    data: Union[str, Dict[str, Dict]] = None
    timeouts: InjectStateTimeouts = None
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
                 timeouts: InjectStateTimeouts = None,
                 transition: Union[str, Transition] = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        # duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
