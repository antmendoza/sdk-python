from __future__ import annotations

import copy
from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.hydrate import ComplexTypeOf, SimpleTypeOf, UnionTypeOf, HydratableParameter
from serverlessworkflow.sdk.tobedone.workflow_exec_timeout import WorkflowExecTimeOut


class ContinueAsDef:
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

        Fields(locals(), kwargs, ContinueAsDef.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):

        if p_key == 'data':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(dict)]))

        if p_key == 'workflowExecTimeOut':
            return HydratableParameter(value=p_value).hydrateAs(ComplexTypeOf(WorkflowExecTimeOut))

        return copy.deepcopy(p_value)
