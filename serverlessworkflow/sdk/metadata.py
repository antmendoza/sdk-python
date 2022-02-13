from typing import Dict

from serverlessworkflow.sdk.class_properties import Properties


class Metadata(Dict[str, str]):

    def __init__(self,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
