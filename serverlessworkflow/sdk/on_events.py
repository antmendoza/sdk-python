from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.enums import ActionMode
from serverlessworkflow.sdk.event_data_filter import EventDataFilter
from serverlessworkflow.sdk.test import Attributes


class OnEvents:
    eventRefs: [str] = None
    actionMode: ActionMode = None
    actions: [Action] = None
    eventDataFilter: EventDataFilter = None

    def __init__(self,
                 eventRefs: [str] = None,
                 actionMode: ActionMode = None,
                 actions: [Action] = None,
                 eventDataFilter: EventDataFilter = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
