from serverlessworkflow.sdk.class_properties import ClassProperties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class OperationStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 actionExecTimeOut: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
