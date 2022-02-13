from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Properties


class ProduceEventDef:
    eventRef: str = None
    data: (str | Dict[str, Dict]) = None
    contextAttributes: Dict[str, str] = None

    def __init__(self,
                 eventRef: str = None,
                 data: (str | Dict[str, Dict]) = None,
                 contextAttributes: Dict[str, str] = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
