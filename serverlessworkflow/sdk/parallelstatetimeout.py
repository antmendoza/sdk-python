from serverlessworkflow.sdk.stateexectimeout import StateExecTimeOut


class ParallelStateTimeOut:
    stateExecTimeOut: StateExecTimeOut = None
    branchExecTimeOut: str = None  # BranchExecTimeOut