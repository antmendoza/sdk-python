from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class CallbackStateTimeOuts:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    eventTimeOut: str = None  # EventTimeOut