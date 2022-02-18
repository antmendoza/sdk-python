import copy

from serverlessworkflow.sdk.tobedone.class_properties import Fields
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef
from serverlessworkflow.sdk.tobedone.hydrate import ArrayTypeOf, HydratableParameter


class Transition:
    nextState: str = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None

    def __init__(self,
                 nextState: str = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 **kwargs):
        Fields(locals(), kwargs, Transition.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'produceEvents':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(ProduceEventDef))

        return copy.deepcopy(p_value)
