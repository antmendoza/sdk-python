from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef


class Transition:
    nextState: str = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None

    def __init__(self,
                 nextState: str = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
