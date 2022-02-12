from typing import Union

from serverlessworkflow.sdk.class_properties import ClassProperties


class RetryDef:
    name: str = None
    delay: str = None
    maxDelay: str = None
    increment: str = None
    multiplier: Union[int, str] = None
    maxAttempts: Union[int, str] = None
    jitter: Union[int, str] = None

    def __init__(self,
                 name: str = None,
                 delay: str = None,
                 maxDelay: str = None,
                 increment: str = None,
                 multiplier: Union[int, str] = None,
                 maxAttempts: Union[int, str] = None,
                 jitter: Union[int, str] = None,
                 **kwargs):

        ClassProperties(locals(), kwargs, ClassProperties.dummy).set_to_object(self)
