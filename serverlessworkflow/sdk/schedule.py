from typing import Union

from serverlessworkflow.sdk.cron_def import CronDef
from serverlessworkflow.sdk.class_properties import ClassProperties


class Schedule:
    interval: str = None
    cron: Union[str, CronDef] = None
    timezone: str = None

    def __init__(self,
                 interval: str = None,
                 cron: Union[str, CronDef] = None,
                 timezone: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
