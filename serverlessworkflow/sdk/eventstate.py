from typing import Union

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.onevents import Onevents
from serverlessworkflow.sdk.statedatafilter import Statedatafilter
from serverlessworkflow.sdk.eventstatetimeouts import EventStateTimeOuts
from serverlessworkflow.sdk.transition import Transition




class Eventstate:
    id: str = None
    name: str = None
    type: 'event' = None
    exclusive: bool = None
    onEvents: [Onevents] = None
    timeouts: EventStateTimeOuts = None
    stateDataFilter: Statedatafilter = None
    onErrors: [Error] = None
    transition: Union[str, Transition] = None
    end: Union[bool, End] = None
    compensatedBy: str = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: 'event' = None,
                 exclusive: bool = None,
                 onEvents: [Onevents] = None,
                 timeouts: EventStateTimeOuts = None,
                 stateDataFilter: Statedatafilter = None,
                 onErrors: [Error] = None,
                 transition: Union[str, Transition] = None,
                 end: Union[bool, End] = None,
                 compensatedBy: str = None,
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
