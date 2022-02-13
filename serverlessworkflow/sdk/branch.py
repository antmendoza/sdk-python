from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.branch_timeout import BranchTimeOut
from serverlessworkflow.sdk.class_properties import Properties


class Branch:
    name: str = None
    timeouts: BranchTimeOut = None
    actions: [Action] = None

    def __init__(self,
                 name: str = None,
                 timeouts: BranchTimeOut = None,
                 actions: [Action] = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
