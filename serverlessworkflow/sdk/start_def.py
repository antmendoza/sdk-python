from typing import Union

from serverlessworkflow.sdk.schedule import Schedule
from serverlessworkflow.sdk.attributes import Attributes


class StartDef:
    stateName: str = None
    schedule: Union[str, Schedule] = None

    def __init__(self,
                 stateName: str = None,
                 schedule: Union[str, Schedule] = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
