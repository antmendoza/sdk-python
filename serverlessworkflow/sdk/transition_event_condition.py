from typing import Union

from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.class_properties import ClassProperties
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

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
