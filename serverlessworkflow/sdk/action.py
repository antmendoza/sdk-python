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
            property_value = Action.load_function_ref(property_value)
        if property_key == 'eventRef':
            property_value = Action.load_event_ref(property_value)
        if property_key == 'subFlowRef':
            property_value = Action.load_sub_flow_ref(property_value)
        if property_key == 'sleep':
            property_value = Action.load_sleep(property_value)
        if property_key == 'actionDataFilter':
            property_value = Action.load_action_data_filter(property_value)
        return property_value

    @staticmethod
    def load_function_ref(function):
        if type(function) is str:
            return function

        return FunctionRef(**function) if type(function) is not FunctionRef else function

    @staticmethod
    def load_action_data_filter(action_df):
        if type(action_df) is str:
            return action_df

        return ActionDataFilter(**action_df) if type(action_df) is not ActionDataFilter else action_df

    @staticmethod
    def load_sub_flow_ref(value):
        if type(value) is str:
            return value

        return SubFlowRef(**value) if type(value) is not SubFlowRef else value

    @staticmethod
    def load_event_ref(value):
        return EventRef(**value) if type(value) is not EventRef else value

    @staticmethod
    def load_sleep(value):
        return Sleep(**value) if type(value) is not Sleep else value
