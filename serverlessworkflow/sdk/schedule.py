from typing import Union

from serverlessworkflow.sdk.crondef import CronDef


class Schedule:
    interval:str = None
    cron: Union[str, CronDef] = None
    timezone: str = None

    def __init__(self,
                 interval:str = None,
                 cron: Union[str, CronDef] = None,
                 timezone: str = None,
                 **kwargs):

        # duplicated
        for local in list(locals()):
            if local in ["self", "kwargs"]:
                continue
            value = locals().get(local)
            if not value:
                continue
            if value == "true":
                value = True
            # duplicated

            self.__setattr__(local.replace("_", ""), value)

        # duplicated
        for k in kwargs.keys():
            value = kwargs[k]
            if value == "true":
                value = True

            self.__setattr__(k.replace("_", ""), value)
            # duplicated
