from __future__ import annotations

import copy

from serverlessworkflow.sdk.action import Action, Parameter
from serverlessworkflow.sdk.callback_state_timeout import CallbackStateTimeOut
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.error import Error
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.hydrate import ComplexType, ArrayOfType
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.state import State
from serverlessworkflow.sdk.state_data_filter import StateDataFilter
from serverlessworkflow.sdk.transition import Transition


class CallbackState(State):
    id: str = None
    name: str = None
    type: str = None
    action: Action = None
    eventRef: str = None
    timeouts: CallbackStateTimeOut = None
    eventDataFilter: EventDataFilter = None
    stateDataFilter: StateDataFilter = None
    onErrors: [Error] = None
    transition: (str | Transition) = None
    end: (str | End) = None
    compensatedBy: str = None
    usedForCompensation: bool = None
    metadata: Metadata = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 action: Action = None,
                 eventRef: str = None,
                 timeouts: CallbackStateTimeOut = None,
                 eventDataFilter: EventDataFilter = None,
                 stateDataFilter: StateDataFilter = None,
                 onErrors: [Error] = None,
                 transition: (str | Transition) = None,
                 end: (str | End) = None,
                 compensatedBy: str = None,
                 usedForCompensation: bool = None,
                 metadata: Metadata = None,
                 **kwargs):

        Fields(locals(), kwargs, Fields.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        result = copy.deepcopy(p_value)

        if p_key == 'action':
            result = Parameter(value=p_value).hydrateAs(ComplexType(Action))

        if p_key == 'timeouts':
            result = Parameter(value=p_value).hydrateAs(ComplexType(CallbackStateTimeOut))

        if p_key == 'eventDataFilter':
            result = Parameter(value=p_value).hydrateAs(ComplexType(EventDataFilter))

        if p_key == 'stateDataFilter':
            result = Parameter(value=p_value).hydrateAs(ComplexType(StateDataFilter))

        if p_key == 'onErrors':
            result = Parameter(value=p_value).hydrateAs(ArrayOfType(Error))

        return result