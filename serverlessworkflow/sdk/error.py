from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Properties
from serverlessworkflow.sdk.end import End
from serverlessworkflow.sdk.transition import Transition


class Error:
    errorRef: str = None
    errorRefs: [str] = None
    transition: (str | Transition) = None
    end: (str | End) = None

    def __init__(self,
                 errorRef: str = None,
                 errorRefs: [str] = None,
                 transition: (str | Transition) = None,
                 end: (str | End) = None,
                 **kwargs):
        Properties(locals(), kwargs, Properties.default).set_to_object(self)
