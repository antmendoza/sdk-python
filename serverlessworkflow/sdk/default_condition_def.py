from typing import Union

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.class_properties import ClassProperties
from serverlessworkflow.sdk.transition import Transition


class DefaultConditionDef:
    transition: Union[str, Transition] = None
    end: Union[bool, End] = None

    def __init__(self,
                 transition: Union[str, Transition] = None,
                 end: Union[bool, End] = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
