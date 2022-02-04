from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class CallbackStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    eventTimeOut: str = None  # EventTimeOut