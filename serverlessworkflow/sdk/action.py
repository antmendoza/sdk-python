from __future__ import annotations

import copy
from typing import Any

from serverlessworkflow.sdk.action_data_filter import ActionDataFilter
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.event_ref import EventRef
from serverlessworkflow.sdk.function_ref import FunctionRef
from serverlessworkflow.sdk.hydrate import ComplexType
from serverlessworkflow.sdk.sleep import Sleep
from serverlessworkflow.sdk.sub_flow_ref import SubFlowRef


class Parameter:
    def __init__(self, value: Any):
        self.complex_type = None
        self.simple_type = None
        self.value = value

    def hydrateAsUnionOf(self, simple_type, complex_type):
        self.simple_type = simple_type
        self.complex_type = complex_type

        if type(self.value) is self.simple_type:
            return self.value

        return self.complex_type(**self.value) if type(self.value) is not self.complex_type else self.value

    def hydrateAs(self, hydratable):
        return hydratable.hydrate(self.value)


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
    jespin: str = None

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
                 eslavida: str = None,
                 **kwargs):

        Action.load_obj(self)

        Fields(locals(), kwargs, Action.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        result = copy.deepcopy(p_value)

        if p_key == 'functionRef':
            ## TODO hydrateUnionType
            result = Parameter(value=p_value).hydrateAsUnionOf(str, FunctionRef)
            #property_value = Action.hydrate_union(property_value, str, FunctionRef)
        if p_key == 'eventRef':
            result = Parameter(value=p_value).hydrateAs(ComplexType(EventRef))
        if p_key == 'subFlowRef':
            result = Action.hydrate_union(p_value, str, SubFlowRef)
        if p_key == 'sleep':
            result = Parameter(value=p_value).hydrateAs(ComplexType(Sleep))
        if p_key == 'actionDataFilter':
            result = Parameter(value=p_value).hydrateAs(ComplexType(ActionDataFilter))
        return result

    @staticmethod
    def hydrate_type(value, Type):

        return Type(**value) if type(value) is not Type else value

    @staticmethod
    def load_obj(obj):

        for prop in obj.__dict__.keys():
            print(prop + " " + str(type(prop)))

        print(dir(obj))
        print(dir(obj))

    @staticmethod
    def hydrate_union(value, ifType, elseType):
        if type(value) is ifType:
            return value

        return elseType(**value) if type(value) is not elseType else value
