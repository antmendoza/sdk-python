import copy

from serverlessworkflow.sdk.serializable import Serializable
from serverlessworkflow.sdk.hydration import ComplexTypeOf, HydratableParameter, Fields


class FunctionRef(Serializable):
    refName: str = None
    arguments: dict[str, dict] = None
    selectionSet: str = None
    invoke: str = None

    def __init__(self,
                 refName: str = None,
                 arguments: dict[str, any] = None,
                 selectionSet: str = None,
                 invoke: str = None,
                 **kwargs):
        Fields(locals(), kwargs, FunctionRef.f_hydration).set_to_object(self)




    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'arguments':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(dict))

        return copy.deepcopy(p_value)
