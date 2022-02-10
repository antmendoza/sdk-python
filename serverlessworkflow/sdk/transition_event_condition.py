from typing import Union

from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.transition import Transition


class TransitionEventCondition:
    name: str = None
    eventRef: str = None
    transition: Union[str, Transition] = None
    eventDataFilter = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 eventRef: str = None,
                 transition: Union[str, Transition] = None,
                 eventDataFilter=None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
