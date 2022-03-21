from __future__ import annotations

import copy

from serverlessworkflow.sdk.hydration import ComplexTypeOf, SimpleTypeOf, UnionTypeOf, HydratableParameter, \
    Fields
from serverlessworkflow.sdk.serializable import Serializable
from serverlessworkflow.sdk.workflow_exec_timeout import WorkflowExecTimeOut


class ContinueAsDef(Serializable):
    workflowId: str = None
    version: str = None
    data: (str | dict) = None
    workflowExecTimeOut: WorkflowExecTimeOut = None

    def __init__(self,
                 workflowId: str = None,
                 version: str = None,
                 data: (str | dict) = None,
                 workflowExecTimeOut: WorkflowExecTimeOut = None,
                 **kwargs):

        Serializable.__init__(self)
        Fields(locals(), kwargs, ContinueAsDef.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'data':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(dict)]))

        if p_key == 'workflowExecTimeOut':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(WorkflowExecTimeOut))

        return copy.deepcopy(p_value)
