from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.continue_as_def import ContinueAsDef
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef


class End:
    terminate: bool = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None
    continueAs: (str | ContinueAsDef) = None

    def __init__(self,
                 terminate: bool = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 continueAs: (str | ContinueAsDef) = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
