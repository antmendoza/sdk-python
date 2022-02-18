from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Fields
from serverlessworkflow.sdk.cron_def import CronDef


class Schedule:
    interval: str = None
    cron: (str | CronDef) = None
    timezone: str = None

    def __init__(self,
                 interval: str = None,
                 cron: (str | CronDef) = None,
                 timezone: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
