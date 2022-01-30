from typing import Union

from serverlessworkflow.sdk.actiondatafilter import Actiondatafilter
from serverlessworkflow.sdk.eventref import Eventref
from serverlessworkflow.sdk.functionref import Functionref
from serverlessworkflow.sdk.sleep import Sleep
from serverlessworkflow.sdk.subflowref import Subflowref


class Action:
    id: str = None
    name: str = None
    functionRef: Union[str, Functionref] = None
    eventRef: Eventref = None
    subFlowRef: Union[str, Subflowref] = None
    sleep: Sleep = None
    retryRef: str = None
    nonRetryableErrors: [str] = None
    retryableErrors: [str] = None
    actionDataFilter: Actiondatafilter = None
    condition: str = None

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 functionRef: Union[str, Functionref] = None,
                 eventRef: Eventref = None,
                 subFlowRef: Union[str, Subflowref] = None,
                 sleep: Sleep = None,
                 retryRef: str = None,
                 nonRetryableErrors: [str] = None,
                 retryableErrors: [str] = None,
                 actionDataFilter: Actiondatafilter = None,
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

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
