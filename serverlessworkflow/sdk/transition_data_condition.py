from __future__ import annotations

import copy

from serverlessworkflow.sdk.hydration import HydratableParameter, UnionTypeOf, SimpleTypeOf, ComplexTypeOf, \
    Fields
from serverlessworkflow.sdk.metadata import Metadata
from serverlessworkflow.sdk.serializable import Serializable
from serverlessworkflow.sdk.transition import Transition


class TransitionDataCondition(Serializable):
    name: str = None
    condition: str = None
    transition: (str | Transition) = None
    metadata: Metadata = None

    def __init__(self,
                 name: str = None,
                 condition: str = None,
                 transition: (str | Transition) = None,
                 metadata: Metadata = None,
                 **kwargs):
        Serializable.__init__(self)
        Fields(locals(), kwargs, TransitionDataCondition.f_hydration).set_to_object(self)

    @staticmethod
    def f_hydration(p_key, p_value):
        if p_key == 'transition':
            return HydratableParameter(value=p_value).hydrateAs(UnionTypeOf([SimpleTypeOf(str),
                                                                             ComplexTypeOf(Transition)]))

        return copy.deepcopy(p_value)
