from typing import Union

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.transition import Transition


class DefaultConditionDef:
    transition: Union[str, Transition] = None
    end: Union[bool, End] = None

    def __init__(self,
                 transition: Union[str, Transition] = None,
                 end: Union[bool, End] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
