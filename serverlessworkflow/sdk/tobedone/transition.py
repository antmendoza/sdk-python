from serverlessworkflow.sdk.class_properties import Fields
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
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
