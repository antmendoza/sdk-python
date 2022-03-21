import copy

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.hydration import HydratableParameter, ArrayTypeOf, ComplexTypeOf, Fields
from serverlessworkflow.sdk.serializable import Serializable


class OnEvents(Serializable):
    eventRefs: [str] = None
    actionMode: str = None
    actions: [Action] = None
    eventDataFilter: EventDataFilter = None

    def __init__(self,
                 eventRefs: [str] = None,
                 actionMode: str = None,
                 actions: [Action] = None,
                 eventDataFilter: EventDataFilter = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration, { 'actionMode': 'sequential' }).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'actions':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Action))

        if p_key == 'eventDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(EventDataFilter))

        return copy.deepcopy(p_value)
