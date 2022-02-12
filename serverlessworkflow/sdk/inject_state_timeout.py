from serverlessworkflow.sdk.class_properties import ClassProperties
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class InjectStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
