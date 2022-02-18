import copy

from serverlessworkflow.sdk.action import Action
from serverlessworkflow.sdk.branch_timeout import BranchTimeOut
from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import ArrayTypeOf, ComplexTypeOf, HydratableParameter


class Branch:
    name: str = None
    timeouts: BranchTimeOut = None
    actions: [Action] = None

    def __init__(self,
                 name: str = None,
                 timeouts: BranchTimeOut = None,
                 actions: [Action] = None,
                 **kwargs):
        Fields(locals(), kwargs, Branch.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        result = copy.deepcopy(p_value)

        if p_key == 'timeouts':
            result = HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(BranchTimeOut))

        if p_key == 'actions':
            result = HydratableParameter(value=p_value).hydrateAs(ArrayTypeOf(Action))

        return result
