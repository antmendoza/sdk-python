from __future__ import annotations

import copy

from serverlessworkflow.sdk.action_data_filter import ActionDataFilter
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.event_ref import EventRef
from serverlessworkflow.sdk.function_ref import FunctionRef
from serverlessworkflow.sdk.hydrate import ComplexType, UnionTypeOf, SimpleType, HydratableParameter
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

        Fields(locals(), kwargs, Action.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        parameter = HydratableParameter(value=p_value)
        if p_key == 'functionRef':
            return parameter.hydrateAs(UnionTypeOf([SimpleType(str), ComplexType(FunctionRef)]))
        if p_key == 'eventRef':
            return parameter.hydrateAs(ComplexType(EventRef))
        if p_key == 'subFlowRef':
            return parameter.hydrateAs(UnionTypeOf([SimpleType(str), ComplexType(SubFlowRef)]))
        if p_key == 'sleep':
            return parameter.hydrateAs(ComplexType(Sleep))
        if p_key == 'actionDataFilter':
            return parameter.hydrateAs(ComplexType(ActionDataFilter))

        return copy.deepcopy(p_value)
