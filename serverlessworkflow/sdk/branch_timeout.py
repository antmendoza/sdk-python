from serverlessworkflow.sdk.class_properties import ClassProperties


class BranchTimeOut:
    actionExecTimeOut: str = None  # ActionExecTimeOut
    branchExecTimeOut: str = None  # BranchExecTimeOut

    def __init__(self,
                 actionExecTimeOut: str = None,
                 branchExecTimeOut: str = None,
                 **kwargs):
        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
