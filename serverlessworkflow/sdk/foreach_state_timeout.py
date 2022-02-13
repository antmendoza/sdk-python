from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class ForEachStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 actionExecTimeOut: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
