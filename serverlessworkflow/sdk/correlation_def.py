from serverlessworkflow.sdk.class_properties import Fields


class CorrelationDef:
    contextAttributeName: str = None
    contextAttributeValue: str = None

    def __init__(self,
                 contextAttributeName: str = None,
                 contextAttributeValue: str = None,
                 **kwargs):
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
