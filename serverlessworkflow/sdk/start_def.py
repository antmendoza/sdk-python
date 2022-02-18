from __future__ import annotations

import copy

from serverlessworkflow.sdk.tobedone.class_properties import Fields
from serverlessworkflow.sdk.schedule import Schedule
from serverlessworkflow.sdk.tobedone.hydrate import SimpleTypeOf, ComplexTypeOf, UnionTypeOf, HydratableParameter


class StartDef:
    stateName: str = None
    schedule: (str | Schedule) = None

    def __init__(self,
                 stateName: str = None,
                 schedule: (str | Schedule) = None,
                 **kwargs):
        Fields(locals(), kwargs, StartDef.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'schedule':
            return HydratableParameter(value=p_value).hydrateAs(
                UnionTypeOf([SimpleTypeOf(str), ComplexTypeOf(Schedule)]))

        return copy.deepcopy(p_value)
