from typing import Union

from serverlessworkflow.sdk.schedule import Schedule
from serverlessworkflow.sdk.class_properties import ClassProperties


class StartDef:
    stateName: str = None
    schedule: Union[str, Schedule] = None

    def __init__(self,
                 stateName: str = None,
                 schedule: Union[str, Schedule] = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
