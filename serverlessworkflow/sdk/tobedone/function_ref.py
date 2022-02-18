import copy
from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import ComplexTypeOf, HydratableParameter


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

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'arguments':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(Dict))

        return copy.deepcopy(p_value)
