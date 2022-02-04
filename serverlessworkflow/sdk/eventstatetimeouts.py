from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class EventStateTimeOuts:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    eventTimeOut: str = None  # EventTimeOut