from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.enums import ActionMode
from serverlessworkflow.sdk.event_data_filter import EventDataFilter


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
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
