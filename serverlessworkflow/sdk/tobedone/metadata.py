from typing import Dict

from serverlessworkflow.sdk.class_properties import Fields


class Metadata(Dict[str, str]):

    def __init__(self,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
