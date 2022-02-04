from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class EventBasedSwitchStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    eventTimeOut: str = None  # EventTimeOut