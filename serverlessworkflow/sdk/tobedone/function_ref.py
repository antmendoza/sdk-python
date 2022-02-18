from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields



class FunctionRef:
    refName: str = None
    arguments: Dict[str, Dict] = None
    selectionSet: str = None
    invoke: str = None

    def __init__(self,
                 refName: str = None,
                 arguments: Dict[str, Dict] = None,
                 selectionSet: str = None,
                 invoke: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
