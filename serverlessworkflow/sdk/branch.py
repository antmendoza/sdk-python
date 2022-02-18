import copy

from serverlessworkflow.sdk.action import Action, Parameter
from serverlessworkflow.sdk.branch_timeout import BranchTimeOut
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.hydrate import ArrayOf, ComplexType


class Branch:
    name: str = None
    timeouts: BranchTimeOut = None
    actions: [Action] = None

    def __init__(self,
                 name: str = None,
                 timeouts: BranchTimeOut = None,
                 actions: [Action] = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        result = copy.deepcopy(p_value)

        if p_key == 'timeouts':
            result = Parameter(value=p_value).hydrateAs(ComplexType(BranchTimeOut))

        if p_key == 'actions':
            result = Parameter(value=p_value).hydrateAs(ArrayOf(Action))

        return result
