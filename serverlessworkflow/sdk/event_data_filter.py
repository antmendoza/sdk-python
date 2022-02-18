from serverlessworkflow.sdk.class_properties import Fields


class EventDataFilter:
    useData: bool = None
    data: str = None
    toStateData: str = None

    def __init__(self,
                 useData: bool = None,
                 data: str = None,
                 toStateData: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
