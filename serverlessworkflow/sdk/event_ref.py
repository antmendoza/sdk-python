from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields



class EventRef:
    triggerEventRef: str = None
    resultEventRef: str = None
    resultEventTimeOut: str = None
    data: (str | Dict) = None
    contextAttributes: Dict[str, str] = None
    invoke: str = None

    def __init__(self,
                 triggerEventRef: str = None,
                 resultEventRef: str = None,
                 data: (str | Dict) = None,
                 contextAttributes: Dict[str, str] = None,
                 invoke: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
