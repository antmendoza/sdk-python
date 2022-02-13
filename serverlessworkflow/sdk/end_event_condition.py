from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.metadata import Metadata


class EndEventCondition:
    name: str = None
    eventRef: str = None
    end: (str | End) = None
    eventDataFilter: EventDataFilter = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 eventRef: str = None,
                 end: (str | End) = None,
                 eventDataFilter: EventDataFilter = None,
                 metadata: Metadata = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
