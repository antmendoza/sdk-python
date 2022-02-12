from typing import Union, Dict

from serverlessworkflow.sdk.class_properties import ClassProperties


class ProduceEventDef:
    eventRef: str = None
    data: Union[str, Dict[str, Dict]] = None
    contextAttributes: Dict[str, str] = None

    def __init__(self,
                 eventRef: str = None,
                 data: Union[str, Dict[str, Dict]] = None,
                 contextAttributes: Dict[str, str] = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
