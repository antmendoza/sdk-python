from serverlessworkflow.sdk.class_properties import ClassProperties


class CorrelationDef:
    contextAttributeName: str = None
    contextAttributeValue: str = None

    def __init__(self,
                 contextAttributeName: str = None,
                 contextAttributeValue: str = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
