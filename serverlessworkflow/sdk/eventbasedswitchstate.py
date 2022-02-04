from typing import Union

from serverlessworkflow.sdk.defaultconditiondef import Defaultconditiondef
from serverlessworkflow.sdk.enddeventcondition import Enddeventcondition
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.statedatafilter import Statedatafilter
from serverlessworkflow.sdk.eventbasedswitchstatetimeouts import EventBasedSwitchStateTimeOuts
from serverlessworkflow.sdk.transitioneventcondition import Transitioneventcondition


class Eventbasedswitchstate:
    id: str = None
    name: str = None
    type: str = None
    stateDataFilter: Statedatafilter = None
    timeouts: EventBasedSwitchStateTimeOuts = None
    eventConditions: Union[Transitioneventcondition, Enddeventcondition] = None  # Eventcondition
    onErrors: [Error] = None
    defaultCondition: Defaultconditiondef = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: 'switch' = None,
                 stateDataFilter: Statedatafilter = None,
                 timeouts: EventBasedSwitchStateTimeOuts = None,
                 eventConditions: Union[Transitioneventcondition, Enddeventcondition] = None,  # Eventcondition
                 onErrors: [Error] = None,
                 defaultCondition: Defaultconditiondef = None,
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
