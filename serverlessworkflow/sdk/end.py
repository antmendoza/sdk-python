from typing import Union

from serverlessworkflow.sdk.continue_as_def import ContinueAsDef
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef
from serverlessworkflow.sdk.class_properties import ClassProperties


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

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
