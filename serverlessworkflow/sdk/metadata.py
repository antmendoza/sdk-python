from typing import Dict

from serverlessworkflow.sdk.attributes import Attributes


class Metadata(Dict[str, str]):

    def __init__(self,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
