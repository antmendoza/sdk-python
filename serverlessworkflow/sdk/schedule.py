from typing import Union

from serverlessworkflow.sdk.cron_def import CronDef
from serverlessworkflow.sdk.test import Attributes


class Schedule:
    interval: str = None
    cron: Union[str, CronDef] = None
    timezone: str = None

    def __init__(self,
                 interval: str = None,
                 cron: Union[str, CronDef] = None,
                 timezone: str = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
