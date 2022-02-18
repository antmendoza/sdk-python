from serverlessworkflow.sdk.tobedone.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, ComplexTypeOf
from serverlessworkflow.sdk.state_exec_timeout import StateExecTimeOut


class SleepStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 **kwargs):
        Fields(locals(), kwargs, SleepStateTimeOut.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'stateExecTimeOut':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(StateExecTimeOut))
