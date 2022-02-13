from serverlessworkflow.sdk.class_properties import Properties


class BranchTimeOut:
    actionExecTimeOut: str = None  # ActionExecTimeOut
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 actionExecTimeOut: str = None,
                 branchExecTimeOut: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
