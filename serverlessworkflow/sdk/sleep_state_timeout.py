from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class SleepStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
