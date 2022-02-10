from typing import Union

from serverlessworkflow.sdk.continue_as_def import ContinueAsDef
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef
from serverlessworkflow.sdk.attributes import Attributes


class End:
    terminate: bool = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None
    continueAs: Union[str, ContinueAsDef] = None

    def __init__(self,
                 terminate: bool = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 continueAs: Union[str, ContinueAsDef] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
