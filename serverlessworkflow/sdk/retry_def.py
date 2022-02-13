from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties


class RetryDef:
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
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
