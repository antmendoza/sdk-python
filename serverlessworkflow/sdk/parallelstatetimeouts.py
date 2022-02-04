from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class ParallelStateTimeOuts:
    stateExecTimeOut: StateExecTimeOut = None
    branchExecTimeOut: str = None  # BranchExecTimeOut