from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.tobedone.schedule import Schedule


class StartDef:
    stateName: str = None
    schedule: (str | Schedule) = None

    def __init__(self,
                 stateName: str = None,
                 schedule: (str | Schedule) = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
