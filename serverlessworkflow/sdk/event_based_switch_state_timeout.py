from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class EventBasedSwitchStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    eventTimeOut: str = None  # EventTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 eventTimeOut: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
