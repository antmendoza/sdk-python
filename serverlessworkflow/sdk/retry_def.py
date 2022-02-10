from typing import Union

from serverlessworkflow.sdk.attributes import Attributes


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

        Attributes(locals(), kwargs, Attributes.dummy).set_to_object(self)
