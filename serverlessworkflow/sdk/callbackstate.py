from typing import Union

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.eventdatafilter import Eventdatafilter
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.statedatafilter import Statedatafilter
from serverlessworkflow.sdk.callbackstatetimeouts import CallbackStateTimeOuts
from serverlessworkflow.sdk.transition import Transition


class Callbackstate:
    id: str = None
    name: str = None
    type: 'callback' = None
    action: Action = None
    eventRef: str = None
    timeouts: CallbackStateTimeOuts = None
    eventDataFilter: Eventdatafilter = None
    stateDataFilter: Statedatafilter = None
    onErrors: [Error] = None
    transition: Union[str, Transition] = None
    end: Union[bool, End] = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: 'callback' = None,
                 action: Action = None,
                 eventRef: str = None,
                 timeouts: CallbackStateTimeOuts = None,
                 eventDataFilter: Eventdatafilter = None,
                 stateDataFilter: Statedatafilter = None,
                 onErrors: [Error] = None,
                 transition: Union[str, Transition] = None,
                 end: Union[bool, End] = None,
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
