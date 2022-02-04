from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class ForEachStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    actionExecTimeOut: str = None  # ActionExecTimeOut