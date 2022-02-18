from __future__ import annotations

from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields


class ProduceEventDef:
    eventRef: str = None
    data: (str | dict) = None
    contextAttributes: dict[str, str] = None

    def __init__(self,
                 eventRef: str = None,
                 data: (str | dict) = None,
                 contextAttributes: dict[str, str] = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
