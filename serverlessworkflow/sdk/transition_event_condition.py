from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.transition import Transition


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
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
