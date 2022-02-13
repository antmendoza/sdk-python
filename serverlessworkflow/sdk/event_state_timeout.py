from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class EventStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    eventTimeOut: str = None  # EventTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 actionExecTimeOut: str = None,
                 eventTimeOut: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
