from typing import Union

from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.transition import Transition


class TransitionDataCondition:
    name: str = None
    condition: str = None
    transition: Union[str, Transition] = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 condition: str = None,
                 transition: Union[str, Transition] = None,
                 metadata: Metadata = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
