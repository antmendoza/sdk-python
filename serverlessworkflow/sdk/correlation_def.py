from serverlessworkflow.sdk.class_properties import Properties


class CorrelationDef:
    contextAttributeName: str = None
    contextAttributeValue: str = None

    def __init__(self,
                 contextAttributeName: str = None,
                 contextAttributeValue: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
