from __future__ import annotations

from serverlessworkflow.sdk.action_data_filter import ActionDataFilter
from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.event_ref import EventRef
from serverlessworkflow.sdk.function_ref import FunctionRef
from serverlessworkflow.sdk.sleep import Sleep
from serverlessworkflow.sdk.sub_flow_ref import SubFlowRef


class Action:
    id: str = None
    name: str = None
    functionRef: (str | FunctionRef) = None
    eventRef: EventRef = None
    subFlowRef: (str | SubFlowRef) = None
    sleep: Sleep = None
    retryRef: str = None
    nonRetryableErrors: [str] = None
    retryableErrors: [str] = None
    actionDataFilter: ActionDataFilter = None
    condition: str = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 functionRef: (str | FunctionRef) = None,
                 eventRef: EventRef = None,
                 subFlowRef: (str | SubFlowRef) = None,
                 sleep: Sleep = None,
                 retryRef: str = None,
                 nonRetryableErrors: [str] = None,
                 retryableErrors: [str] = None,
                 actionDataFilter: ActionDataFilter = None,
                 condition: str = None,
                 **kwargs):

        Properties(locals(), kwargs, Action.load_properties).set_to_object(self)

    @staticmethod
    def load_properties(property_key, property_value):
        if property_key == 'functionRef':
            property_value = Action.hydrate_as_union(property_value, str, FunctionRef)
        if property_key == 'eventRef':
            property_value = Action.hydrate_as_type(property_value, EventRef)
        if property_key == 'subFlowRef':
            property_value = Action.hydrate_as_union(property_value, str, SubFlowRef)
        if property_key == 'sleep':
            property_value = Action.hydrate_as_type(property_value, Sleep)
        if property_key == 'actionDataFilter':
            property_value = Action.hydrate_as_type(property_value, ActionDataFilter)
        return property_value

    @staticmethod
    def hydrate_as_type(value, Type):

        return Type(**value) if type(value) is not Type else value

    @staticmethod
    def hydrate_as_union(value, ifType, elseType):
        if type(value) is ifType:
            return value

        return elseType(**value) if type(value) is not elseType else value
