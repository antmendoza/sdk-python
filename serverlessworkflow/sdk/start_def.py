from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.schedule import Schedule


class StartDef:
    stateName: str = None
    schedule: (str | Schedule) = None

    def __init__(self,
                 stateName: str = None,
                 schedule: (str | Schedule) = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
