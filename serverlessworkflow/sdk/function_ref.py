from typing import Dict

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.enums import Invoke


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
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
