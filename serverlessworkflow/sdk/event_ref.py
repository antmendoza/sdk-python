from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.enums import Invoke


class EventRef:
    triggerEventRef: str = None
    resultEventRef: str = None
    resultEventTimeOut: str = None
    data: (str | Dict[str, Dict]) = None
    contextAttributes: Dict[str, str] = None
    invoke: Invoke = None

    def __init__(self,
                 triggerEventRef: str = None,
                 resultEventRef: str = None,
                 data: (str | Dict[str, Dict]) = None,
                 contextAttributes: Dict[str, str] = None,
                 invoke: Invoke = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
