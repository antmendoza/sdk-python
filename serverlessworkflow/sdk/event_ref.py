from typing import Dict, Union

from serverlessworkflow.sdk.enums import Invoke
from serverlessworkflow.sdk.class_properties import ClassProperties


class EventRef:
    triggerEventRef: str = None
    resultEventRef: str = None
    resultEventTimeOut: str = None
    data: Union[str, Dict[str, Dict]] = None
    contextAttributes: Dict[str, str] = None
    invoke: Invoke = None

    def __init__(self,
                 triggerEventRef: str = None,
                 resultEventRef: str = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 contextAttributes: Dict[str, str] = None,
                 invoke: Invoke = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
