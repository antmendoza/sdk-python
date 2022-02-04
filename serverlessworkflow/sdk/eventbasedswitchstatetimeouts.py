from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class EventBasedSwitchStateTimeOuts:
    stateExecTimeOut: StateExecTimeOut = None
    eventTimeOut: str = None  # EventTimeOut