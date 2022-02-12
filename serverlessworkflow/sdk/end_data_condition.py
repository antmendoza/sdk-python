from typing import Union

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.class_properties import ClassProperties


class EndDataCondition:
    name: str = None
    condition: str = None
    end: Union[bool, End] = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 condition: str = None,
                 end: Union[bool, End] = None,
                 metadata: Metadata = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
