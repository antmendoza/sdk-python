from serverlessworkflow.sdk.produce_event_def import ProduceEventDef
from serverlessworkflow.sdk.test import Attributes


class Transition:
    nextState: str = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None

    def __init__(self,
                 nextState: str = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
