import copy

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, ArrayTypeOf, ComplexTypeOf


class OnEvents:
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
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'action':
            return HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Action))

        if p_key == 'eventDataFilter':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(EventDataFilter))

        return copy.deepcopy(p_value)
