from __future__ import annotations

from serverlessworkflow.sdk.class_properties import Fields
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
        Fields(locals(), kwargs, Fields.no_hydration).set_to_object(self)
