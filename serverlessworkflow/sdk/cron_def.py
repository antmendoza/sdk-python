from serverlessworkflow.sdk.test import Attributes


class CronDef:
    expression: str = None
    validUntil: str = None

    def __init__(self,
                 expression: str = None,
                 validUntil: str = None,
                 **kwargs):

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
