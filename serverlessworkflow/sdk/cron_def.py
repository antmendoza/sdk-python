from serverlessworkflow.sdk.class_properties import Properties


class CronDef:
    expression: str = None
    validUntil: str = None

    def __init__(self,
                 expression: str = None,
                 validUntil: str = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
