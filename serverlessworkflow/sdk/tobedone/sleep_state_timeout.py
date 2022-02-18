from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.state_exec_timeout import StateExecTimeOut


class SleepStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
