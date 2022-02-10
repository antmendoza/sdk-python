from typing import Union, Dict

from serverlessworkflow.sdk.attributes import Attributes


class ProduceEventDef:
    eventRef: str = None
    data: Union[str, Dict[str, Dict]] = None
    contextAttributes: Dict[str, str] = None

    def __init__(self,
                 eventRef: str = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 contextAttributes: Dict[str, str] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
