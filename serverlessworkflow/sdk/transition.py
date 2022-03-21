import copy

from serverlessworkflow.sdk.hydration import ArrayTypeOf, HydratableParameter, Fields
from serverlessworkflow.sdk.produce_event_def import ProduceEventDef
from serverlessworkflow.sdk.serializable import Serializable


class Transition(Serializable):
    nextState: str = None
    produceEvents: [ProduceEventDef] = None
    compensate: bool = None

    def __init__(self,
                 nextState: str = None,
                 produceEvents: [ProduceEventDef] = None,
                 compensate: bool = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Transition.f_hydration,
               {'compensate': False}
               ).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'produceEvents':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(ProduceEventDef))

        return copy.deepcopy(p_value)
