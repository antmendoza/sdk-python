from typing import Union

from serverlessworkflow.sdk.action_data_filter import ActionDataFilter
from serverlessworkflow.sdk.event_ref import EventRef
from serverlessworkflow.sdk.function_ref import FunctionRef
from serverlessworkflow.sdk.sleep import Sleep
from serverlessworkflow.sdk.sub_flow_ref import SubFlowRef


class Action:
    id: str = None
    name: str = None
    functionRef: Union[str, FunctionRef] = None
    eventRef: EventRef = None
    subFlowRef: Union[str, SubFlowRef] = None
    sleep: Sleep = None
    retryRef: str = None
    nonRetryableErrors: [str] = None
    retryableErrors: [str] = None
    actionDataFilter: ActionDataFilter = None
    condition: str = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 functionRef: Union[str, FunctionRef] = None,
                 eventRef: EventRef = None,
                 subFlowRef: Union[str, SubFlowRef] = None,
                 sleep: Sleep = None,
                 retryRef: str = None,
                 nonRetryableErrors: [str] = None,
                 retryableErrors: [str] = None,
                 actionDataFilter: ActionDataFilter = None,
                 condition: str = None,
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

            if local == 'functionRef':
                value = Action.load_function_ref(value)

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            if k == 'functionRef':
                value = Action.load_function_ref(value)

            self.__setattr__(k.replace("_", ""), value)
            # duplicated

    @staticmethod
    def load_function_ref(function):
        if type(function) is str:
            return function

        return FunctionRef(**function) if type(function) is not FunctionRef else function
