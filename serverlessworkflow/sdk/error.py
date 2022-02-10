from typing import Union

from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.attributes import Attributes
from serverlessworkflow.sdk.transition import Transition


class Error:
    errorRef: str = None
    errorRefs: [str] = None
    transition: Union[str, Transition] = None
    end: Union[bool, End] = None

    def __init__(self,
                 errorRef: str = None,
                 errorRefs: [str] = None,
                 transition: Union[str, Transition] = None,
                 end: Union[bool, End] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
