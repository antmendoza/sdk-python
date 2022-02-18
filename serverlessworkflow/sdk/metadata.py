from typing import Dict

from serverlessworkflow.sdk.tobedone.class_properties import Fields


class Metadata(Dict[str, str]):

    def __init__(self,
                 **kwargs):
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
