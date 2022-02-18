from serverlessworkflow.sdk.class_properties import Fields


class BranchTimeOut:
    actionExecTimeOut: str = None  # ActionExecTimeOut
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 actionExecTimeOut: str = None,
                 branchExecTimeOut: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
