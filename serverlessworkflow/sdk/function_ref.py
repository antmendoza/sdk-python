import copy

from serverlessworkflow.sdk.tobedone.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import ComplexTypeOf, HydratableParameter


class FunctionRef:
    refName: str = None
    arguments: dict[str, dict] = None
    selectionSet: str = None
    invoke: str = None

    def __init__(self,
                 refName: str = None,
                 arguments: dict[str, dict] = None,
                 selectionSet: str = None,
                 invoke: str = None,
                 **kwargs):
        Fields(locals(), kwargs, FunctionRef.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'arguments':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(dict))

        return copy.deepcopy(p_value)
