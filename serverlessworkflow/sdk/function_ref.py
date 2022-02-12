from typing import Dict

from serverlessworkflow.sdk.enums import Invoke
from serverlessworkflow.sdk.class_properties import ClassProperties


class FunctionRef:
    refName: str = None
    arguments: Dict[str, Dict] = None
    selectionSet: str = None
    invoke: Invoke = None

    def __init__(self,
                 refName: str = None,
                 arguments: Dict[str, Dict] = None,
                 selectionSet: str = None,
                 invoke: Invoke = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
