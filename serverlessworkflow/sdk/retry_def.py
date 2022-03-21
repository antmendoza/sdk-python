from __future__ import annotations

from serverlessworkflow.sdk.hydration import Fields
from serverlessworkflow.sdk.serializable import Serializable


class RetryDef(Serializable):
    name: str = None
    delay: str = None
    maxDelay: str = None
    increment: str = None
    multiplier: (int | str) = None
    maxAttempts: (int | str) = None
    jitter: (int | str) = None

    def __init__(self,
                 name: str = None,
                 delay: str = None,
                 maxDelay: str = None,
                 increment: str = None,
                 multiplier: (int | str) = None,
                 maxAttempts: (int | str) = None,
                 jitter: (int | str) = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, Fields.default_hydration).set_to_object(self)
