from typing import Dict

from serverlessworkflow.sdk.class_properties import ClassProperties


class Metadata(Dict[str, str]):

    def __init__(self,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
