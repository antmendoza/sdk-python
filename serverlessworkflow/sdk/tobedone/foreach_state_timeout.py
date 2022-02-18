from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.state_exec_timeout import StateExecTimeOut


class ForEachStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 actionExecTimeOut: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
