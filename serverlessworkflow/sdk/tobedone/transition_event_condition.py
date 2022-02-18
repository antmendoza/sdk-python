from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.metadata import Metadata
from serverlessworkflow.sdk.tobedone.transition import Transition


class TransitionEventCondition:
    name: str = None
    eventRef: str = None
    transition: (str | Transition) = None
    eventDataFilter = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 eventRef: str = None,
                 transition: (str | Transition) = None,
                 eventDataFilter=None,
                 metadata: Metadata = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
