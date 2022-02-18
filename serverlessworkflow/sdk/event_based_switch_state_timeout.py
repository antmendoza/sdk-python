import copy

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import HydratableParameter, ComplexTypeOf
from serverlessworkflow.sdk.tobedone.state_exec_timeout import StateExecTimeOut


class EventBasedSwitchStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    eventTimeOut: str = None  # EventTimeOut

    def __init__(self,
                 stateExecTimeOut: StateExecTimeOut = None,
                 eventTimeOut: str = None,
                 **kwargs):
        Fields(locals(), kwargs, EventBasedSwitchStateTimeOut.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'stateExecTimeOut':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(StateExecTimeOut))

        return copy.deepcopy(p_value)
