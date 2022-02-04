from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class EventStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut
    eventTimeOut: str = None  # EventTimeOut